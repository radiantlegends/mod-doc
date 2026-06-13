def load_file(path: str) -> str:
    """
    Reads a text file and returns its contents as a string.

    Args:
        path (str): The filesystem path to the file.

    Returns:
        str: The full contents of the file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def assemble_docs(doc1: str, doc2: str) -> str:
    """
    Concatenates two documentation strings with spacing.

    Args:
        doc1 (str): The first document.
        doc2 (str): The second document.

    Returns:
        str: The combined document with a blank line between sections.
    """
    return doc1 + "\n\n" + doc2

def main():
    """
    Orchestrates the loading and assembly of documentation modules.
    """
    a = load_file("modules/intro.md")
    b = load_file("modules/receiving.md")
    result = assemble_docs(a, b)
    print(result)

if __name__ == "__main__":
    main()