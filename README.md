# Modular Documentation
A clean, simple CLI tool that assembles modular documentation from text files.

## MVP
Read a folder of text files and assemble them into a single document based on a user‑provided list of modules.

## CLI Commands
- docgen build build_order.txt output.txt
    - build_order.txt: file containing module load order
    - output.txt: destination for assembled documentation

## Core Logic
1. File Loader
    - Reads module files.
    - Returns their contents as strings.
2. Assembler
    - Takes a list of module names.
    - Loads each module.
    - Concatenates them with spacing.
3. CLI Handler
    - Parses command-line arguments.
    - Calls the assembler.
    - Writes to the output file.
