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

def write_file(path: str, document: str):
    """
    Write the assembled document to the designated filepath.

    Args:
        path (str): The destination to write to.
        document (str): The text to write.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(document)