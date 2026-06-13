import requests
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_vector_db():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return Chroma(
        persist_directory="vector_db",
        embedding_function=embedding_model
    )


def ask_ollama(prompt, model="llama3.2"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    return response.json()["response"]


def generate_answer(question, k=3):
    vector_db = get_vector_db()
    retrieved_docs = vector_db.similarity_search(question, k=k)

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are a healthcare document assistant.

Answer the question using ONLY the context below.
If the answer is not found in the context, say:
"I could not find this information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

    answer = ask_ollama(prompt)

    return answer, retrieved_docs