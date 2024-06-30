import json
import random

from utils.utils_llm import INSTRUCTION_PROMPT, USER_PROMPT


def get_opcode_messages(opcode, params):
    handlers = {
        '0': opcode_0x,
        '1': opcode_1nnn,
        '2': opcode_2nnn,
        '3': opcode_3xkk,
        '4': opcode_4xkk,
        '5': opcode_5xy0,
        '6': opcode_6xkk,
        '7': opcode_7xkk,
        '8': opcode_8xy,
        '9': opcode_9xy0,
        'a': opcode_Annn,
        'b': opcode_Bnnn,
        'c': opcode_Cxkk,
        'd': opcode_Dxyn,
        'e': opcode_Ex,
        'f': opcode_Fx,
    }
    handler = handlers.get(opcode[2])
    if handler:
        return handler(opcode, params)
    return None


def opcode_00E0(opcode, params):
    """
    00E0 - CLS
    Clear the display.
    """
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": "display.clear()"

                })
            }
        ]
    }


def opcode_00EE(opcode, params):
    """
    00EE - RET
    Return from a subroutine.

    The interpreter sets the program counter to the address at the top of the stack,
    then subtracts 1 from the stack pointer.
    """
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": "PC = stack.pop()",
                    "block_end": "True"
                })
            }
        ]
    }


def opcode_0x(opcode, params):
    if opcode == '0x00ee':
        return opcode_00EE(opcode, params)
    elif opcode == '0x00e0':
        return opcode_00E0(opcode, params)


def opcode_1nnn(opcode, params):
    """
    1nnn - JP addr
    Jump to location nnn.

    The interpreter sets the program counter to nnn.
    """
    nnn = params['nnn']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"PC = {nnn}",
                    "marker": nnn,
                    "block": nnn,
                    "block_end": "True"
                })
            }
        ]
    }


def opcode_2nnn(opcode, params):
    """
    2nnn - CALL addr
    Call subroutine at nnn.

    The interpreter increments the stack pointer, then puts the current PC on the top of the stack.
    The PC is then set to nnn.
    """
    nnn = params['nnn']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"stack.append(PC); PC = {nnn}",
                    "marker": nnn,
                    "block": nnn,
                })
            }
        ]
    }


def opcode_3xkk(opcode, params):
    """
    3xkk - SE Vx, byte
    Skip next instruction if Vx = kk.

    The interpreter compares register Vx to kk, and if they are equal, increments the program counter by 2.
    """
    x = params['x']
    kk = params['kk']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": f"{INSTRUCTION_PROMPT}\n\nAddress: {address}, Instruction: {opcode}"
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"PC += 2 if V[{x}] == {kk} else 0",
                    "block": f"{address + 4}"
                })
            }
        ]
    }


def opcode_4xkk(opcode, params):
    """
    4xkk - SNE Vx, byte
    Skip next instruction if Vx != kk.

    The interpreter compares register Vx to kk, and if they are not equal, increments the program counter by 2.
    """
    x = params['x']
    kk = params['kk']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": f"{INSTRUCTION_PROMPT}\n\nAddress: {address}, Instruction: {opcode}"
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"PC += 2 if V[{x}] != {kk} else 0",
                    "block": f"{address + 4}"
                })
            }
        ]
    }


def opcode_5xy0(opcode, params):
    """
    5xy0 - SE Vx, Vy
    Skip next instruction if Vx = Vy.

    The interpreter compares register Vx to register Vy, and if they are equal, increments the program counter by 2.
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": f"{INSTRUCTION_PROMPT}\n\nAddress: {address}, Instruction: {opcode}"
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"PC += 2 if V[{x}] == V[{y}] else 0",
                    "block": f"{address + 4}"
                })
            }
        ]
    }


def opcode_6xkk(opcode, params):
    """
    6xkk - LD Vx, byte
    Set Vx = kk.

    The interpreter puts the value kk into register Vx.
    """
    x = params['x']
    kk = params['kk']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"V[{x}] = {kk}"
                })
            }
        ]
    }


def opcode_7xkk(opcode, params):
    """
    7xkk - ADD Vx, byte
    Set Vx = Vx + kk.

    Adds the value kk to the value of register Vx, then stores the result in Vx.
    """
    x = params['x']
    kk = params['kk']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"V[{x}] = (V[{x}] + {kk}) & 0xFF"
                })
            }
        ]
    }


def opcode_8xy0(opcode, params):
    """
    8xy0 - LD Vx, Vy
    Set Vx = Vy.

    Stores the value of register Vy in register Vx.
    # Set V[0xA] to V[0xB]
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"V[{x}] = V[{y}]"
                })
            }
        ]
    }


def opcode_8xy1(opcode, params):
    """
    8xy1 - OR Vx, Vy
    Set Vx = Vx OR Vy.

    Performs a bitwise OR on the values of Vx and Vy, then stores the result in Vx.
    A bitwise OR compares the corresponding bits from two values, and if either bit is 1,
    then the same bit in the result is also 1. Otherwise, it is 0.
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"V[{x}] = V[{x}] | V[{y}]"
                })
            }
        ]
    }


def opcode_8xy2(opcode, params):
    """
    8xy2 - AND Vx, Vy
    Set Vx = Vx AND Vy.

    Performs a bitwise AND on the values of Vx and Vy, then stores the result in Vx.
    A bitwise AND compares the corresponding bits from two values, and if both bits are 1,
    then the same bit in the result is also 1. Otherwise, it is 0.
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"V[{x}] = V[{x}] & V[{y}]"
                })
            }
        ]
    }


def opcode_8xy3(opcode, params):
    """
    8xy3 - XOR Vx, Vy
    Set Vx = Vx XOR Vy.

    Performs a bitwise exclusive OR on the values of Vx and Vy, then stores the result in Vx.
    An exclusive OR compares the corresponding bits from two values, and if the bits are not both the same,
    then the corresponding bit in the result is set to 1. Otherwise, it is 0.
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"V[{x}] = V[{x}] ^ V[{y}]"
                })
            }
        ]
    }


def opcode_8xy4(opcode, params):
    """
    8xy4 - ADD Vx, Vy
    Set Vx = Vx + Vy, set VF = carry.

    The values of Vx and Vy are added together. If the result is greater than 8 bits (i.e., > 255),
    VF is set to 1, otherwise 0. Only the lowest 8 bits of the result are kept, and stored in Vx.
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    #"decoded_instruction": f"result = V[{x}] + V[{y}]; V[0xF] = 1 if result > 0xFF else 0; V[{x}] = result & 0xFF"
                    "decoded_instruction": f"result = V[{x}] + V[{y}]; V[{x}] = result & 0xFF; V[0xF] = 1 if result > 0xFF else 0; "
                })
            }
        ]
    }


def opcode_8xy5(opcode, params):
    """
    8xy5 - SUB Vx, Vy
    Set Vx = Vx - Vy, set VF = NOT borrow.

    If Vx > Vy, then VF is set to 1, otherwise 0. Then Vy is subtracted from Vx, and the result is stored in Vx.
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    #"decoded_instruction": f"V[0xF] = 1 if V[{x}] > V[{y}] else 0; V[{x}] = (V[{x}] - V[{y}]) & 0xFF"
                    "decoded_instruction": f"borrow = 1 if V[{x}] >= V[{y}] else 0; V[{x}] = (V[{x}] - V[{y}]) & 0xFF; V[0xF] = borrow"
                })
            }
        ]
    }


def opcode_8xy6(opcode, params):
    """
    8xy6 - SHR Vx {, Vy}
    Set Vx = Vx SHR 1.

    If the least-significant bit of Vx is 1, then VF is set to 1, otherwise 0.
    Then Vx is divided by 2.
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    #"decoded_instruction": f"V[0xF] = V[{x}] & 0x1; V[{x}] >>= 1"
                    "decoded_instruction": f"lsb = V[{x}] & 0x1; V[{x}] = V[{x}] >> 1; V[0xF] = lsb"
                })
            }
        ]
    }


def opcode_8xy7(opcode, params):
    """
    8xy7 - SUBN Vx, Vy
    Set Vx = Vy - Vx, set VF = NOT borrow.

    If Vy > Vx, then VF is set to 1, otherwise 0. Then Vx is subtracted from Vy, and the result is stored in Vx.
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    #"decoded_instruction": f"V[0xF] = 1 if V[{y}] > V[{x}] else 0; V[{x}] = (V[{y}]- V[{x}]) & 0xFF"
                    "decoded_instruction": f"not_borrow = 1 if V[{y}] >= V[{x}] else 0; V[{x}] = (V[{y}] - V[{x}]) & 0xFF; V[0xF] = not_borrow"
                })
            }
        ]
    }


def opcode_8xyE(opcode, params):
    """
    8xyE - SHL Vx {, Vy}
    Set Vx = Vx SHL 1.

    If the most-significant bit of Vx is 1, then VF is set to 1, otherwise to 0. Then Vx is multiplied by 2.
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    #"decoded_instruction": f"V[0xF] = (V[{x}] >> 7) & 0x1; V[{x}] = (V[{x}] << 1) & 0xFF"
                    "decoded_instruction": f"msb = (V[{y}] & 0x80) >> 7; V[{x}] = (V[{y}] << 1) & 0xFF; V[0xF] = msb"
                })
            }
        ]
    }


def opcode_8xy(opcode, params):
    sub_opcode = opcode[-1]

    if sub_opcode == '0':
        return opcode_8xy0(opcode, params)
    elif sub_opcode == '1':
        return opcode_8xy1(opcode, params)
    elif sub_opcode == '2':
        return opcode_8xy2(opcode, params)
    elif sub_opcode == '3':
        return opcode_8xy3(opcode, params)
    elif sub_opcode == '4':
        return opcode_8xy4(opcode, params)
    elif sub_opcode == '5':
        return opcode_8xy5(opcode, params)
    elif sub_opcode == '6':
        return opcode_8xy6(opcode, params)
    elif sub_opcode == '7':
        return opcode_8xy7(opcode, params)
    elif sub_opcode == 'e':
        return opcode_8xyE(opcode, params)


def opcode_9xy0(opcode, params):
    """
    9xy0 - SNE Vx, Vy
    Skip next instruction if Vx != Vy.

    The values of Vx and Vy are compared, and if they are not equal, the program counter is increased by 2.
    """
    x = params['x']
    y = params['y']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": f"{INSTRUCTION_PROMPT}\n\nAddress: {address}, Instruction: {opcode}"
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"PC += 2 if V[{x}] != V[{y}] else 0",
                    "block": f"{address + 4}"
                })
            }
        ]
    }


def opcode_Annn(opcode, params):
    """
    Annn - LD I, addr
    Set I = nnn.

    The value of register I is set to nnn.
    """
    nnn = params['nnn']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"I = {nnn}",
                    "marker": nnn,
                })
            }
        ]
    }


def opcode_Bnnn(opcode, params):
    """
    Bnnn - JP V0, addr
    Jump to location nnn + V0.

    The program counter is set to nnn plus the value of V0.
    """
    nnn = params['nnn']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"PC = {nnn} + V[0]",
                    "block": nnn,
                    "block_end": "True"
                })
            }
        ]
    }


def opcode_Cxkk(opcode, params):
    """
    Cxkk - RND Vx, byte
    Set Vx = random byte AND kk.

    The interpreter generates a random number from 0 to 255, which is then ANDed with the value kk.
    The results are stored in Vx.
    """
    kk = params['kk']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"V[{params['x']}] = random.randint(0, 255) & {kk}",
                })
            }
        ]
    }


def opcode_Dxyn(opcode, params):
    """
    Dxyn - DRW Vx, Vy, nibble
    Display n-byte sprite starting at memory location I at (Vx, Vy), set VF = collision.

    The interpreter reads n bytes from memory, starting at the address stored in I. These bytes are then displayed
    as sprites on screen at coordinates (Vx, Vy). Sprites are XORed onto the existing screen. If this causes any
    pixels to be erased, VF is set to 1, otherwise it is set to 0. If the sprite is positioned so part of it is
    outside the coordinates of the display, it wraps around to the opposite side of the screen.
    """
    x = params['x']
    y = params['y']
    n = params['n']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"draw_sprite({x}, {y}, {n})"
                })
            }
        ]
    }


def opcode_Ex9E(opcode, params):
    """
    Ex9E - SKP Vx
    Skip next instruction if key with the value of Vx is pressed.

    Checks the keyboard, and if the key corresponding to the value of Vx is currently in the down position, PC is increased by 2.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"PC += 2 if keys[V[{x}]] else 0",
                    "block": f"{address + 4} "
                })
            }
        ]
    }


def opcode_ExA1(opcode, params):
    """
    ExA1 - SKNP Vx
    Skip next instruction if key with the value of Vx is not pressed.

    Checks the keyboard, and if the key corresponding to the value of Vx is currently in the up position, PC is increased by 2.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"PC += 2 if not keys[V[{x}]] else 0",
                    "block": f"{address + 4}"
                })
            }
        ]
    }


def opcode_Ex(opcode, params):
    sub_opcode = opcode[-2:]
    if sub_opcode == '9e':
        return opcode_Ex9E(opcode, params)
    elif sub_opcode == 'a1':
        return opcode_ExA1(opcode, params)


def opcode_Fx07(opcode, params):
    """
    Fx07 - LD Vx, DT
    Set Vx = delay timer value.

    The value of DT is placed into Vx.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"V[{x}] = DT",
                })
            }
        ]
    }


def opcode_Fx0A(opcode, params):
    """
    Fx0A - LD Vx, K
    Wait for a key press, store the value of the key in Vx.

    All execution stops until a key is pressed, then the value of that key is stored in Vx.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"waiting_keypress = True; keypress_register = {x}"
                })
            }
        ]
    }


def opcode_Fx15(opcode, params):
    """
    Fx15 - LD DT, Vx
    Set delay timer = Vx.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"DT = V[{x}]"
                })
            }
        ]
    }


def opcode_Fx18(opcode, params):
    """
    Fx18 - LD ST, Vx
    Set sound timer = Vx.

    ST is set equal to the value of Vx.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"ST = V[{x}]"
                })
            }
        ]
    }


def opcode_Fx1E(opcode, params):
    """
    Fx1E - ADD I, Vx
    Set I = I + Vx.

    The values of I and Vx are added, and the result is stored in I.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"I = (I + V[{x}]) & 0xFFFF"
                })
            }
        ]
    }


def opcode_Fx29(opcode, params):
    """
    Fx29 - LD F, Vx
    Set I = location of sprite for digit Vx.

    The value of I is set to the location for the hexadecimal sprite corresponding to the value of Vx.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"I = (V[{x}] & 0x0F) * 5"
                })
            }
        ]
    }


def opcode_Fx33(opcode, params):
    """
    Fx33 - LD B, Vx
    Store BCD representation of Vx in memory locations I, I+1, and I+2.

    The interpreter takes the decimal value of Vx, and places the hundreds digit in memory at location I,
    the tens digit at location I+1, and the ones digit at location I+2.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"value = V[{x}]; memory[I] = value // 100; memory[I + 1] = (value // 10) % 10; memory[I + 2] = value % 10"
                })
            }
        ]
    }


def opcode_Fx55(opcode, params):
    """
    Fx55 - LD [I], Vx
    Store registers V0 through Vx in memory starting at location I.

    The interpreter copies the values of registers V0 through Vx into memory, starting at the address in I.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"memory[I:I + {x} + 1] = V[:{x} + 1]"
                })
            }
        ]
    }


def opcode_Fx65(opcode, params):
    """
    Fx65 - LD Vx, [I]
    Read registers V0 through Vx from memory starting at location I.

    The interpreter reads values from memory starting at location I into registers V0 through Vx.
    """
    x = params['x']
    address = random.randint(0, 65000)
    return {
        "messages": [
            {
                "role": "user",
                "content": USER_PROMPT.format(INSTRUCTION_PROMPT, address, opcode)
            },
            {
                "role": "assistant",
                "content": json.dumps({
                    "decoded_instruction": f"V[:{x} + 1] = memory[I:I + {x} + 1]"
                })
            }
        ]
    }


def opcode_Fx(opcode, params):
    sub_opcode = opcode[-2:]

    if sub_opcode == '07':
        return opcode_Fx07(opcode, params)
    elif sub_opcode == '0a':
        return opcode_Fx0A(opcode, params)
    elif sub_opcode == '15':
        return opcode_Fx15(opcode, params)
    elif sub_opcode == '18':
        return opcode_Fx18(opcode, params)
    elif sub_opcode == '1e':
        return opcode_Fx1E(opcode, params)
    elif sub_opcode == '29':
        return opcode_Fx29(opcode, params)
    elif sub_opcode == '33':
        return opcode_Fx33(opcode, params)
    elif sub_opcode == '55':
        return opcode_Fx55(opcode, params)
    elif sub_opcode == '65':
        return opcode_Fx65(opcode, params)
