import pygame
import sys

from cpu import CPU
from emulator import Emulator
from utils.utils_debug import start_emulator_debug_thread
from utils.utils_emulator import load_disassembly, generate_beep_sound, KEY_MAP

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 320
PIXEL_SIZE = 10


def main(disassembly_path, debug_mode=False):

    pygame.init()
    pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Chipstral Emulator')
    clock = pygame.time.Clock()

    emulator = Emulator(cpu_type=CPU)

    load_disassembly(emulator, disassembly_path)

    beep_sound = generate_beep_sound()

    if debug_mode:
        start_emulator_debug_thread(emulator.cpu)

    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000 // 60)  # Decrement at a rate of 60 Hz

    key_down_event = None
    waiting_for_key_release = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == timer_event:
                if emulator.cpu.DT > 0:
                    emulator.cpu.DT -= 1
                if emulator.cpu.ST > 0:
                    if not pygame.mixer.get_busy():
                        beep_sound.play(-1)
                    emulator.cpu.ST -= 1
                else:
                    if pygame.mixer.get_busy():
                        pygame.mixer.stop()
            elif event.type == pygame.KEYDOWN:
                if event.key in KEY_MAP:
                    emulator.cpu.keys[KEY_MAP[event.key]] = 1
                    if emulator.cpu.waiting_keypress:
                        key_down_event = event.key
                        emulator.cpu.keypress(event.key)
                        waiting_for_key_release = True
            elif event.type == pygame.KEYUP:
                if event.key in KEY_MAP:
                    emulator.cpu.keys[KEY_MAP[event.key]] = 0
                    if waiting_for_key_release and event.key == key_down_event:
                        waiting_for_key_release = False
                        emulator.cpu.waiting_keypress = False

        if not emulator.cpu.waiting_keypress and not waiting_for_key_release:
            emulator.cycle()

        screen.fill((0, 0, 0))
        for y in range(32):
            for x in range(64):
                if emulator.display.pixels[y][x] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

        pygame.display.flip()
        clock.tick(600)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python emulator.py <path to disassembly> [--debug]")
        sys.exit(1)

    disassembly_path = sys.argv[1]
    debug_mode = '--debug' in sys.argv

    main(disassembly_path, debug_mode)
