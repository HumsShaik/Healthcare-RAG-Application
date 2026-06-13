import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

from src.document_loader import load_pdf_documents
from src.text_splitter import split_documents

docs = load_pdf_documents()
chunks = split_documents(docs)

print(f"Total pages loaded: {len(docs)}")
print(f"Total chunks created: {len(chunks)}")

if chunks:
    print("\nFirst chunk metadata:")
    print(chunks[0].metadata)

    print("\nFirst chunk preview:")
    print(chunks[0].page_content[:700])