# 🏥 Healthcare RAG Application

An end-to-end Retrieval-Augmented Generation (RAG) application built using Python, LangChain, ChromaDB, Sentence Transformers, Ollama, and Streamlit. The application enables intelligent question answering over healthcare documents including clinical guidelines, compliance policies, and FDA recall notices.

---

## 📌 Project Overview

Healthcare organizations manage large volumes of clinical, regulatory, and compliance documentation. Finding relevant information quickly can be challenging and time-consuming.

This project leverages Retrieval-Augmented Generation (RAG) to enable users to ask natural language questions and receive grounded answers generated from healthcare documents.

The application retrieves relevant document sections using vector similarity search and generates responses using a local Large Language Model (LLM) running through Ollama.

---

## 🎯 Business Problem

Healthcare professionals frequently need to search across:

* Clinical Guidelines
* HIPAA Compliance Documents
* FDA Recall Notices
* Regulatory Documentation
* Patient Safety Policies

Manual review is inefficient and may delay access to critical information.

---

## 💡 Solution

This application:

1. Loads healthcare PDF documents
2. Splits documents into manageable chunks
3. Generates embeddings using Sentence Transformers
4. Stores embeddings in ChromaDB
5. Retrieves relevant content based on user questions
6. Uses Llama 3.2 via Ollama to generate answers grounded in retrieved content

---

## 🛠 Technology Stack

| Component             | Technology            |
| --------------------- | --------------------- |
| Programming Language  | Python                |
| Application Framework | Streamlit             |
| RAG Framework         | LangChain             |
| Embedding Model       | Sentence Transformers |
| Vector Database       | ChromaDB              |
| Local LLM             | Ollama (Llama 3.2)    |
| Document Processing   | PyPDF                 |
| Version Control       | Git & GitHub          |

---

## 📂 Project Structure

```text
Healthcare-RAG-Application/
│
├── app/
│   └── app.py
│
├── data/
│   └── raw/
│
├── notebooks/
│   ├── test_document_loader.py
│   ├── test_text_splitter.py
│   ├── test_vector_store.py
│   ├── test_retriever.py
│   └── test_rag_pipeline.py
│
├── reports/
│   └── screenshots/
│
├── src/
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   ├── rag_pipeline.py
│   ├── build_vector_db.py
│   └── __init__.py
│
├── vector_db/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📄 Documents Used

### FDA Dexcom Recall

Purpose:

* Recall investigation
* Medical device safety
* Regulatory compliance

### HIPAA Privacy Guidance

Purpose:

* Healthcare compliance
* Privacy regulations
* Breach notification requirements

### WHO Diabetes Guideline

Purpose:

* Clinical recommendations
* Diabetes management
* Patient care guidance

---

## ⚙️ Workflow

```text
Healthcare PDFs
        ↓
Document Loader
        ↓
Text Chunking
        ↓
Sentence Transformer Embeddings
        ↓
ChromaDB Vector Database
        ↓
Similarity Retrieval
        ↓
Ollama (Llama 3.2)
        ↓
Grounded Answer Generation
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/HumsShaik/Healthcare-RAG-Application.git

cd Healthcare-RAG-Application
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download Ollama:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

Pull Llama 3.2:

```bash
ollama pull llama3.2
```

Test:

```bash
ollama run llama3.2
```

---

## 🧠 Build Vector Database

After adding PDF files to:

```text
data/raw/
```

Run:

```bash
python src/build_vector_db.py
```

Expected Output:

```text
Documents loaded: 45
Chunks created: 85
Vector database built successfully!
```

---

## ▶️ Run Application

```bash
streamlit run app/app.py
```

Open:

```text
http://localhost:8501
```

---

## 💬 Example Questions

### HIPAA

```text
What does HIPAA say about breach notification?
```

### FDA Recall

```text
Why were Dexcom G7 sensors recalled?
```

### Clinical Guideline

```text
What are the goals of diabetes management?
```

### Patient Safety

```text
What patient safety risks are mentioned in the documents?
```

---

## 📊 Streamlit Features

### 📌 Overview

* Project Summary
* Key Metrics
* Business Problem
* Solution Overview

### 💬 Ask Assistant

* Natural Language Question Answering
* Source-Aware Responses
* Configurable Retrieval

### 📄 Source Documents

* Healthcare Document Inventory
* Document Purpose
* Knowledge Domains

### 🧠 RAG Architecture

* End-to-End Workflow
* Technology Stack
* System Design

---

## 🔑 Key Features

* Healthcare-specific document retrieval
* Local embeddings using Sentence Transformers
* ChromaDB vector search
* Local LLM inference using Ollama
* Retrieval-Augmented Generation (RAG)
* Source-grounded responses
* Streamlit user interface
* Zero API cost implementation

---
##
Live App Link: https://healthcare-rag-application.streamlit.app/
---

## 📈 Skills Demonstrated

### Data Engineering

* Document Processing
* Data Pipelines
* Data Transformation
* Vector Databases

### Artificial Intelligence

* Retrieval-Augmented Generation
* Embeddings
* Semantic Search
* Large Language Models

### Software Engineering

* Python Development
* Modular Architecture
* API Integration
* Streamlit Applications

### Healthcare Analytics

* Clinical Guidelines
* HIPAA Compliance
* FDA Recall Analysis
* Healthcare Knowledge Retrieval

---

## 🔮 Future Enhancements

* Multi-document upload support
* Chat history and memory
* PDF preview functionality
* Citation highlighting
* Evaluation metrics dashboard
* Azure OpenAI integration
* Multi-user authentication
* Cloud deployment

---

## 👩‍💻 Author

**Humera Anjum**

Healthcare Analytics | Data Analytics | Data Engineering | Generative AI

GitHub: https://github.com/HumsShaik

---

## ⭐ Project Summary

Built an end-to-end Healthcare Retrieval-Augmented Generation (RAG) application using LangChain, ChromaDB, Sentence Transformers, Ollama, and Streamlit to enable intelligent question answering across clinical guidelines, HIPAA compliance documentation, and FDA recall notices using local embeddings and a local Large Language Model.
