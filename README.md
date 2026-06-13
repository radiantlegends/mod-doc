# Modular Documentation
A clean, simple CLI tool that assembles modular documentation from text files.

## MVP
Read a folder of text files and assemble them into a single document based on a user‑provided list of modules.

## CLI Commands
- docgen build build_order.txt output.md
    - Create the documentation file using the modules in the provided build order.
    - build_order.txt: file containing module load order information
    - output.md: destination for assembled documentation

## Core Logic
1. File Loader
    - Reads markdown files.
    - Returns their contents as strings.
2. Assembler
    - Takes a list of module names.
    - Loads each module.
    - Concatenates them with spacing.
3. CLI Handler
    - Parses command-line arguments.
    - Calls the assembler.
    - Writes to the output file.

## Milestones
1. ☑ Create a script that:
    - loads two hardcoded files
    - concatenates them
    - prints the result
2. ☑ Read the build_order.txt file:
    - load the build order file
    - parse the build order as a list
3. Assemble an arbitrary number of modules.
    - loop through each module
    - assemble them into one document
4. Add CLI arguments:
    - input list
    - output file
5. Clean up logic:
    - parser
    - assembler
    - cli