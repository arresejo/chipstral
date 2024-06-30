import os
import sys
from disassembler import Disassembler
from utils.utils_debug import start_disassembler_debug_thread


def main(assembly_path, debug_mode=False):
    disassembler = Disassembler()
    disassembler.load_rom(assembly_path)

    if debug_mode:
        start_disassembler_debug_thread(disassembler)

    disassembler.decode()
    disassembly = disassembler.get_disassembly()

    base_name = os.path.splitext(assembly_path)[0]
    output_path = f"{base_name}.chs"

    with open(output_path, "w") as outfile:
        outfile.write(disassembly)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python run_disassembler.py <path to ROM> [--debug]")
        sys.exit(1)

    assembly_path = sys.argv[1]
    debug_mode = '--debug' in sys.argv

    print("Disassembling ROM...")
    main(assembly_path, debug_mode)
    print("Done!")
