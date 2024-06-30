from display import Display
from memory import Memory


class Emulator:
    def __init__(self, cpu_type):
        self.memory = Memory()
        self.display = Display()
        self.cpu = cpu_type(self.memory, self.display)

    def cycle(self):
        self.cpu.fetch_execute_cycle()
