import os
from langchain_community.document_loaders import PyPDFLoader


def load_pdf_documents(data_folder="data/raw"):
    documents = []

    if not os.path.exists(data_folder):
        raise FileNotFoundError(f"Folder not found: {data_folder}")

    for file_name in os.listdir(data_folder):
        if file_name.lower().endswith(".pdf"):
            file_path = os.path.join(data_folder, file_name)

            loader = PyPDFLoader(file_path)
            pdf_docs = loader.load()

            for doc in pdf_docs:
                doc.metadata["source_file"] = file_name

            documents.extend(pdf_docs)

    return documents