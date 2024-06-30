![343855687-f9b1ee6c-f069-4ee1-bf56-56e25223758f-2](https://github.com/arresejo/chipstral/assets/3316147/06845d8d-8268-429c-bb35-95bd422e50e0)


# An LLM Assisted Disassembler

## Introduction

This repository contains the source code for the Chipstral project, created for [the Mistral AI Hackathon](https://mistral.ai/news/2024-ft-hackathon/).

[CHIP-8](https://en.wikipedia.org/wiki/CHIP-8) is a simple interpreted programming language developed in the 1970s, designed to provide an easy way to write video games 8-bit microcomputer.

The Chipstral project integrates both a CHIP-8 disassembler and an emulator.

The disassembler leverages a fine-tuned version of the Mistral 7B language model to decode original CHIP-8 instructions and transcribe them into an assembly file.

The produced assembly files are compatible with the emulator, which executes the code and updates the machine's state in real-time, allowing original ROMs to be played.

![344453395-db0b780c-595b-40c4-8089-e32379c768e8-2](https://github.com/arresejo/chipstral/assets/3316147/a369373b-a54b-4025-a45a-5e40f5ef5f79)


## How It Was Built

A dataset of 68K entries was created by generating random CHIP-8 instructions. For each entry, the expected outcome is the disassembly code, derived from the [technical reference](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM). Python was chosen as the disassembly language to facilitate direct interpretation by the emulator.

A Mistral-7b model was then fine-tuned on this dataset using the [La Plateforme](https://mistral.ai/fr/news/la-plateforme/) API.

The training and validation datasets are available at [🤗 Hugging Face](https://huggingface.co/datasets/arresejo/chipstral).

## Setup Instructions

To get started, first create a virtual environment and install the necessary dependencies:

```bash
pip install -r requirements.txt
```

Next, open the `.env` file and replace `MISTRAL_API_KEY` with your actual Mistral API key.

To launch the disassembler, use the following command. Add the `--debug` flag for debugging mode:
```bash
python run_disassembler.py roms/Chipstral.ch8 [--debug]
```

To launch the emulator, use the following command. Add the `--debug` flag for debugging mode:
```bash
python run_emulator.py roms/Chipstral.chs [--debug]
```

To generate the datasets, use the following command:
```bash
python dataset/generate_dataset.py
```


## ROMs

A custom ROM was developed for this project using [Octo](https://github.com/JohnEarnest/Octo). The source code is available in the project as `Chipstral.8o`.

Other ROMs included in this project are sourced from the [chip8](https://github.com/dmatlack/chip8) repository.


