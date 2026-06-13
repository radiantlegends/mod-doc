from .io_utils import load_file

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

def build_document(build_order: list[str]) -> str:
    """
    Assembles all modules in the build order into one final document.

    Args:
        build_order (list[str]): List of modules to assemble.

    Returns:
        final_doc (str): The combined modules in one document.
    """
    if not build_order:
        return ""

    folder = "modules/"
    
    final_doc = load_file(folder + build_order[0])
    for file_name in build_order[1:]:
        file = folder + file_name
        doc = load_file(file)
        final_doc = assemble_docs(final_doc, doc)
    return final_doc