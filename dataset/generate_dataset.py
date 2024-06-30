import json
import random

from tqdm import tqdm

from dataset.opcode_messages import get_opcode_messages

SEED = 42

NUM_ITEMS_PER_OPCODE = 100

REGISTER_SAMPLE_SIZE = 0xF + 1  # 16 registers
BYTE_SAMPLE_SIZE = 0xFF + 1  # 256 bytes
ADDRESS_SAMPLE_SIZE = 0xFFF + 1  # 4096 addresses

base_opcodes = [
    {"opcode": 0x00E0, "label": "00E0"},  # Clear the display
    {"opcode": 0x00EE, "label": "00EE"},  # Return from subroutine
    {"opcode": 0x1000, "label": "1nnn", "params": ["address"]},  # Jump to location
    {"opcode": 0x2000, "label": "2nnn", "params": ["address"]},  # Call subroutine at
    {"opcode": 0x3000, "label": "3xkk", "params": ["register", "byte"]},  # Skip next instruction if Vx = kk
    {"opcode": 0x4000, "label": "4xkk", "params": ["register", "byte"]},  # Skip next instruction if Vx != kk
    {"opcode": 0x5000, "label": "5xy0", "params": ["register", "register"]},  # Skip next instruction if Vx = Vy
    {"opcode": 0x6000, "label": "6xkk", "params": ["register", "byte"]},  # Set register Vx
    {"opcode": 0x7000, "label": "7xkk", "params": ["register", "byte"]},  # Add to register Vx
    {"opcode": 0x8000, "label": "8xy0", "params": ["register", "register"]},  # Set Vx = Vy
    {"opcode": 0x8001, "label": "8xy1", "params": ["register", "register"]},  # Set Vx = Vx OR Vy
    {"opcode": 0x8002, "label": "8xy2", "params": ["register", "register"]},  # Set Vx = Vx AND Vy
    {"opcode": 0x8003, "label": "8xy3", "params": ["register", "register"]},  # Set Vx = Vx XOR Vy
    {"opcode": 0x8004, "label": "8xy4", "params": ["register", "register"]},  # Add Vy to Vx, set VF = carry
    {"opcode": 0x8005, "label": "8xy5", "params": ["register", "register"]},  # Subtract Vy from Vx, set VF = NOT borrow
    {"opcode": 0x8006, "label": "8xy6", "params": ["register", "register"]},  # Set Vx = Vx SHR 1
    {"opcode": 0x8007, "label": "8xy7", "params": ["register", "register"]},  # Set Vx = Vy - Vx, set VF = NOT borrow
    {"opcode": 0x800E, "label": "8xyE", "params": ["register", "register"]},  # Set Vx = Vx SHL 1
    {"opcode": 0x9000, "label": "9xy0", "params": ["register", "register"]},  # Skip next instruction if Vx != Vy
    {"opcode": 0xA000, "label": "Annn", "params": ["address"]},  # Set index register
    {"opcode": 0xB000, "label": "Bnnn", "params": ["address"]},  # Jump to location nnn + V0
    {"opcode": 0xC000, "label": "Cxkk", "params": ["register", "byte"]},  # Set Vx = random byte AND kk
    {"opcode": 0xD000, "label": "Dxyn", "params": ["register", "register", "nibble"]},  # Display n-byte sprite starting at memory location I at (Vx, Vy), set VF = collision
    {"opcode": 0xE09E, "label": "Ex9E", "params": ["register"]},  # Skip next instruction if key with the value of Vx is pressed
    {"opcode": 0xE0A1, "label": "ExA1", "params": ["register"]},  # Skip next instruction if key with the value of Vx is not pressed
    {"opcode": 0xF007, "label": "Fx07", "params": ["register"]},  # Set Vx = delay timer value
    {"opcode": 0xF00A, "label": "Fx0A", "params": ["register"]},  # Wait for a key press, store the value of the key in Vx
    {"opcode": 0xF015, "label": "Fx15", "params": ["register"]},  # Set delay timer = Vx
    {"opcode": 0xF018, "label": "Fx18", "params": ["register"]},  # Set sound timer = Vx
    {"opcode": 0xF01E, "label": "Fx1E", "params": ["register"]},  # Add Vx to I
    {"opcode": 0xF029, "label": "Fx29", "params": ["register"]},  # Set I = location of sprite for digit Vx
    {"opcode": 0xF033, "label": "Fx33", "params": ["register"]},  # Store BCD representation of Vx in memory locations I, I+1, and I+2
    {"opcode": 0xF055, "label": "Fx55", "params": ["register"]},  # Store registers V0 through Vx in memory starting at location I
    {"opcode": 0xF065, "label": "Fx65", "params": ["register"]},  # Read registers V0 through Vx from memory starting at location I
]


def generate_samples(base, count):
    if base["params"] == ["address"]:
        return [{"opcode": base["opcode"] | addr, "params": {"nnn": hex(addr)}} for addr in
                random.choices(range(0, ADDRESS_SAMPLE_SIZE), k=count)]
    elif base["params"] == ["register", "byte"]:
        samples = []
        for _ in range(count):
            reg = random.choice(range(0x0, REGISTER_SAMPLE_SIZE))
            byte = random.choice(range(0x00, BYTE_SAMPLE_SIZE))
            val = (reg << 8) | byte
            samples.append({"opcode": base["opcode"] | val, "params": {"x": hex(reg), "kk": hex(byte)}})
        return samples
    elif base["params"] == ["register"]:
        return [{"opcode": base["opcode"] | (reg << 8), "params": {"x": hex(reg)}} for reg in
                random.choices(range(0x0, REGISTER_SAMPLE_SIZE), k=count)]
    elif base["params"] == ["register", "register"]:
        samples = []
        for _ in range(count):
            reg_x = random.choice(range(0x0, REGISTER_SAMPLE_SIZE))
            reg_y = random.choice(range(0x0, REGISTER_SAMPLE_SIZE))
            val = (reg_x << 8) | (reg_y << 4)
            samples.append({"opcode": base["opcode"] | val, "params": {"x": hex(reg_x), "y": hex(reg_y)}})
        return samples
    elif base["params"] == ["register", "register", "nibble"]:
        samples = []
        for _ in range(count):
            reg_x = random.choice(range(0x0, REGISTER_SAMPLE_SIZE))
            reg_y = random.choice(range(0x0, REGISTER_SAMPLE_SIZE))
            nibble = random.choice(range(0x0, 0xF + 1))
            val = (reg_x << 8) | (reg_y << 4) | nibble
            samples.append(
                {"opcode": base["opcode"] | val, "params": {"x": hex(reg_x), "y": hex(reg_y), "n": hex(nibble)}})
        return samples
    else:
        raise ValueError(f"Unsupported parameter combination: {base['params']}")


def generate_sampled_opcodes():
    opcodes = []
    labels = []
    params = []

    for base in base_opcodes:
        if "params" not in base:
            samples = [{"opcode": base["opcode"], "params": None} for _ in range(NUM_ITEMS_PER_OPCODE)]
        else:
            samples = generate_samples(base, NUM_ITEMS_PER_OPCODE)

        for sample in samples:
            opcodes.append(sample["opcode"])
            labels.append(base["label"])
            params.append(sample["params"])

    return opcodes, labels, params


def main():
    opcodes, labels, params = generate_sampled_opcodes()

    dataset = []

    for _ in tqdm(range(20), desc="Generating dataset"):
        for opcode, label, param in zip(opcodes, labels, params):
            messages = get_opcode_messages(f"0x{opcode:0{4}x}", param)
            dataset.append(messages)

    random.shuffle(dataset)

    train_size = int(0.96 * len(dataset))
    df_train = dataset[:train_size]
    df_eval = dataset[train_size:]

    with open("chipstral_train.jsonl", "w") as train_file:
        for entry in df_train:
            train_file.write(json.dumps(entry) + "\n")

    with open("chipstral_eval.jsonl", "w") as eval_file:
        for entry in df_eval:
            eval_file.write(json.dumps(entry) + "\n")

    print("Data saved to JSONL files successfully.")


if __name__ == "__main__":
    main()
