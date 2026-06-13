def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def assemble_docs(doc1, doc2):
    return doc1 + "\n\n" + doc2

def main():
    a = load_file("modules/intro.md")
    b = load_file("modules/receiving.md")
    result = assemble_docs(a, b)
    print(result)

if __name__ == "__main__":
    main()