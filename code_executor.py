import ast
import random


class CodeExecutor:

    def __init__(self, cpu):
        self.cpu = cpu

    def execute_code(self, code):
        tree = ast.parse(code, mode='exec')

        exec_env = {
            'random': random,
            'self': self.cpu,
            'PC': self.cpu.PC,
            'I': self.cpu.I,
            'DT': self.cpu.DT,
            'ST': self.cpu.ST,
            'V': self.cpu.V,
            'display': self.cpu.display,
            'memory': self.cpu.memory,
            'draw_sprite': self.cpu.draw_sprite,
            'stack': self.cpu.stack,
            'keys': self.cpu.keys,
            'waiting_keypress': self.cpu.waiting_keypress,
            'keypress_register': self.cpu.keypress_register,
        }

        try:
            exec(compile(tree, filename="<ast>", mode="exec"), exec_env)
        except Exception as e:
            print(f"Error executing code: {e}")


        self.cpu.PC = exec_env['PC']
        self.cpu.I = exec_env['I']
        self.cpu.DT = exec_env['DT']
        self.cpu.ST = exec_env['ST']
        self.cpu.V = exec_env['V']
