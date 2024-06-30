import numpy as np
import pygame

KEY_MAP = {
    pygame.K_1: 0x1,
    pygame.K_2: 0x2,
    pygame.K_3: 0x3,
    pygame.K_4: 0xC,
    pygame.K_q: 0x4,
    pygame.K_w: 0x5,
    pygame.K_e: 0x6,
    pygame.K_r: 0xD,
    pygame.K_a: 0x7,
    pygame.K_s: 0x8,
    pygame.K_d: 0x9,
    pygame.K_f: 0xE,
    pygame.K_z: 0xA,
    pygame.K_x: 0x0,
    pygame.K_c: 0xB,
    pygame.K_v: 0xF,
}


def generate_beep_sound(frequency=440, duration=0.5, volume=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = 0.5 * volume * np.sign(np.sin(2 * np.pi * frequency * t))
    waveform = np.array(waveform * 32767, dtype=np.int16)
    sound = pygame.mixer.Sound(waveform)
    return sound


def load_disassembly(emulator, disassembly_path):
    with open(disassembly_path, 'r') as f:
        disassembly = f.read()
        for line in disassembly.split('\n'):
            if not line:
                continue
            if line[0] == '0':
                address, instruction = line.split('\t')
                address = int(address, 16)
                if instruction.split()[0] == 'DB':
                    emulator.memory.write_byte(address, int(instruction.split()[1], 16))
                else:
                    emulator.cpu.instructions[address] = instruction
