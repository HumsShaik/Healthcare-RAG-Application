import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

from src.rag_pipeline import generate_answer

question = "What does HIPAA say about breach notification?"

answer, sources = generate_answer(question)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(answer)

print("\nSOURCES USED:")
for i, doc in enumerate(sources, start=1):
    print(f"\nSource {i}:")
    print(doc.metadata)
    print(doc.page_content[:300])