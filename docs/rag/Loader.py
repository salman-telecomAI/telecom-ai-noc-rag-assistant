from pathlib import Path

DATA_DIR = Path("data")

def list_documents():
    files = []

    for file in DATA_DIR.rglob("*"):
        if file.is_file():
            files.append(str(file))

    return files


if __name__ == "__main__":
    for document in list_documents():
        print(document)