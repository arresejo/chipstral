import os

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]
model = os.environ["MODEL"]

client = MistralClient(api_key=api_key)

INSTRUCTION_PROMPT = "You're the CHIP-8 Disassembler, interpreting hexadecimal instructions and providing the " \
                     "corresponding disassembly in Python code. Each instruction will be provided in the format of four " \
                     "hexadecimal digits along with the current address in decimal format in the machine's memory. Your task " \
                     "is to understand each instruction and respond with the appropriate Python code that disassembles the " \
                     "instruction into a human-readable format based on the provided address.\n\n"

USER_PROMPT = "{}\n\nAddress: {}, Instruction: {}"


def call_llm(prompt, temperature=0):
    messages = [
        ChatMessage(role='user', content=prompt)
    ]

    response = client.chat(
        model=model,
        messages=messages,
        temperature=temperature,
        response_format={"type": "json_object"},
    )

    return response
