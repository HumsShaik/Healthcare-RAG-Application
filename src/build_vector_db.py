import os
import sys

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

from src.document_loader import load_pdf_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store


def main():
    docs = load_pdf_documents()
    chunks = split_documents(docs)
    create_vector_store(chunks)

    print(f"Documents loaded: {len(docs)}")
    print(f"Chunks created: {len(chunks)}")
    print("Vector database built successfully!")


if __name__ == "__main__":
    main()