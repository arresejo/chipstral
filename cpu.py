from code_executor import CodeExecutor
from utils.utils_emulator import KEY_MAP


class CPU:
    def __init__(self, memory, display):
        self.memory = memory
        self.display = display
        self.V = [0] * 16
        self.I = 0
        self.PC = 0x200
        self.stack = []
        self.DT = 0
        self.ST = 0
        self.keys = [0] * 16
        self.code_executor = CodeExecutor(self)
        self.instructions = {}
        self.waiting_keypress = False
        self.keypress_register = None

    def fetch_execute_cycle(self):
        instruction = self.fetch()
        self.execute(instruction)

    def fetch(self):
        instruction = self.instructions.get(self.PC)
        self.PC += 2
        return instruction

    def keypress(self, key):
        for pygame_key, chip8_key in KEY_MAP.items():
            if key == pygame_key:
                self.V[self.keypress_register] = chip8_key
                self.waiting_keypress = False
                break

    def draw_sprite(self, x, y, n):
        x_coord = self.V[x] % self.display.width
        y_coord = self.V[y] % self.display.height

        self.V[0xF] = 0

        for byte_index in range(n):
            sprite_byte = self.memory.read_byte(self.I + byte_index)
            for bit_index in range(8):
                sprite_pixel = (sprite_byte >> (7 - bit_index)) & 1
                if sprite_pixel:
                    xi = (x_coord + bit_index) % self.display.width
                    yi = (y_coord + byte_index) % self.display.height
                    display_pixel = self.display.get_pixel(xi, yi)

                    if sprite_pixel & display_pixel:
                        self.V[0xF] = 1

                    new_pixel = sprite_pixel ^ display_pixel
                    self.display.set_pixel(xi, yi, new_pixel)

    def execute(self, instruction):
        if instruction is not None:
            self.code_executor.execute_code(instruction)
