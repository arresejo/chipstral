import threading
import json

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live

console = Console()


def format_registers(cpu):
    column1 = [f"[bold blue]V{i:X}[/bold blue]: [bold green]{cpu.V[i]:02X}[/bold green]" for i in range(16)]

    special_registers = [
        f"[bold blue]PC[/bold blue]: [bold green]{cpu.PC:03X}[/bold green]",
        f"[bold blue]I[/bold blue]:  [bold green]{cpu.I:03X}[/bold green]",
        f"[bold blue]ST[/bold blue]: [bold green]{cpu.ST:02X}[/bold green]",
        f"[bold blue]DT[/bold blue]: [bold green]{cpu.DT:02X}[/bold green]",
    ]

    stack_lines = ["\n", "[bold blue]STACK[/bold blue]:"]
    stack_lines.extend([f"[bold green]{value:03X}[/bold green]" for value in cpu.stack])

    column2 = [f"{reg}" for reg in special_registers] + stack_lines

    return column1, column2


def display_emulator_debug(cpu):
    with Live(console=console, refresh_per_second=1) as live:
        while True:
            layout = create_emulator_debug_layout(cpu)
            live.update(layout)


def create_emulator_debug_layout(cpu):
    window_size = 24
    instructions = []
    start_pc = max(0x200, cpu.PC - (window_size // 2) * 2)
    end_pc = min(len(cpu.memory), start_pc + window_size * 2)

    for pc in range(start_pc, end_pc, 2):
        if pc in cpu.instructions:
            instruction = f"{pc:03X}: {cpu.instructions[pc]}"
            if pc == cpu.PC:
                instructions.append(f"[bold red]{instruction}[/bold red]")
            else:
                instructions.append(instruction)

    layout = Layout()

    column1, column2 = format_registers(cpu)

    upper_layout = Layout()
    upper_layout.split_row(
        Layout(Panel("\n".join(instructions), title="[bold blue]Instructions[/bold blue]"), ratio=4),
        Layout(Panel("\n".join(column1))),
        Layout(Panel("\n".join(column2)))
    )

    layout.update(upper_layout)

    return layout


def start_emulator_debug_thread(cpu):
    emulator_debug_thread = threading.Thread(target=display_emulator_debug, args=(cpu,), daemon=True)
    emulator_debug_thread.start()
    return emulator_debug_thread


def display_disassembler_debug(disassembler):
    with Live(console=console, refresh_per_second=1) as live:
        while True:
            layout = create_disassembler_layout(disassembler)
            live.update(layout)


def create_disassembler_layout(disassembler):
    window_size = 12
    layout = Layout()

    if len(disassembler.disassembly_history) == 0 or len(disassembler.llm_history) == 0:
        return layout

    disassembly_history = [
        f"Address: [bold cyan]{address}[/bold cyan]\tOpcode: [bold yellow]{opcode_hex}[/bold yellow]\tDecoded: [bold red]{decoded}[/bold red]"
        for address, opcode_hex, decoded in disassembler.disassembly_history
    ]

    prompt, response = disassembler.llm_history[-1]
    prompt = prompt.replace('\n\n', '\n')

    llm_entry = f"Prompt: [bold magenta]{prompt}[/bold magenta]\n\nResponse: [bold red]{json.dumps(response)}[/bold red]"

    layout.split_column(
        Layout(Panel(llm_entry, title="LLM")),
        Layout(Panel("\n".join(disassembly_history[-window_size:]), title="Disassembly")),
    )

    return layout


def start_disassembler_debug_thread(disassembler):
    display_thread = threading.Thread(target=display_disassembler_debug, args=(disassembler,), daemon=True)
    display_thread.start()
    return display_thread
