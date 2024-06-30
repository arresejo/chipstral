import json
from collections import deque

from memory import Memory
from utils.utils_llm import call_llm, USER_PROMPT, INSTRUCTION_PROMPT


class Disassembler:

    def __init__(self):
        self.memory = Memory()
        self.rom_size = 0
        self.markers = []
        self.active_blocks = []
        self.total_blocks = []
        self.decoded_instructions = {}
        self.active_address = 0x200
        self.block_end = False
        self.disassembly_history = []
        self.llm_history = deque(maxlen=5)

    def load_rom(self, rom_path):
        memory = Memory()
        with open(rom_path, 'rb') as f:
            rom_data = f.read()
        for i in range(len(rom_data)):
            memory.write_byte(0x200 + i, rom_data[i])
        self.rom_size = len(rom_data)
        self.memory = memory

    def decode(self, address=0x200):
        self.block_end = False
        self.active_address = address

        while self.block_end is False:

            if self.active_address in self.decoded_instructions:
                self.block_end = True
                break

            if self.active_address - 0x200 + 1 > self.rom_size:
                self.block_end = True
                break

            opcode = self.memory.read_byte(self.active_address) << 8 | self.memory.read_byte(self.active_address + 1)
            opcode_hex = f'0x{opcode:04x}'

            prompt = USER_PROMPT.format(INSTRUCTION_PROMPT, self.active_address, opcode_hex)
            response = call_llm(prompt)

            json_response = json.loads(response.choices[0].message.content)

            self.decoded_instructions[self.active_address] = json_response["decoded_instruction"]

            if "marker" in json_response:
                self.add_marker(json_response["marker"])
            if "block" in json_response:
                self.add_block(json_response["block"])
            if "block_end" in json_response:
                self.block_end = True

            self.llm_history.append((prompt, json_response))
            self.disassembly_history.append(
                (hex(self.active_address), opcode_hex, json_response['decoded_instruction']))

            self.active_address += 2

        if len(self.active_blocks) > 0:
            self.decode(self.active_blocks.pop())

    def add_marker(self, marker):
        if isinstance(marker, str) and marker[:2] == '0x':
            marker = int(marker, 16)
        else:
            marker = int(marker)
        self.markers.append(marker)

    def add_block(self, block):
        if isinstance(block, str) and block[:2] == '0x':
            block = int(block, 16)
        else:
            block = int(block)
        if block not in self.total_blocks:
            self.active_blocks.append(block)
            self.total_blocks.append(block)

    def get_disassembly(self):
        address = 0x200
        disassembly = ""

        while address < 0x200 + self.rom_size:
            disassembly += "0x{:04x}".format(address)

            if address in self.decoded_instructions:
                line = f"\t{self.decoded_instructions[address]}\n"
                address += 2
            else:
                data = self.memory.read_byte(address)
                line = f"\tDB 0x{data:02x}\n"
                address += 1

            disassembly += line

        return disassembly
