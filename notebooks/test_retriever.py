import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding_model
)

query = "What does HIPAA say about breach notification?"

results = vector_db.similarity_search(
    query,
    k=3
)

print("\nQUESTION:")
print(query)

print("\nTOP MATCHES:\n")

for i, doc in enumerate(results, start=1):
    print("=" * 80)
    print(f"Result {i}")
    print("=" * 80)
    print(doc.page_content[:1000])
    print("\n")