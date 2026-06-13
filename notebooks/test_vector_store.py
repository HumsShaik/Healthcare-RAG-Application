import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

from src.document_loader import load_pdf_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store

docs = load_pdf_documents()

chunks = split_documents(docs)

vector_db = create_vector_store(chunks)

print(f"Documents Loaded: {len(docs)}")
print(f"Chunks Created: {len(chunks)}")

print("\nVector database created successfully!")