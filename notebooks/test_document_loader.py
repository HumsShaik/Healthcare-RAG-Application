import sys
import os

# Get project root
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

# Add project root to Python path
sys.path.insert(0, project_root)

print("Project Root:", project_root)

from src.document_loader import load_pdf_documents

docs = load_pdf_documents()

print(f"\nTotal pages loaded: {len(docs)}")

if docs:
    print("\nFirst document metadata:")
    print(docs[0].metadata)

    print("\nFirst 500 characters:")
    print(docs[0].page_content[:500])