import sys
import os
import streamlit as st

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

from src.rag_pipeline import generate_answer


st.set_page_config(
    page_title="Healthcare RAG Assistant",
    page_icon="🏥",
    layout="wide"
)


st.sidebar.title("🏥 Healthcare RAG")
st.sidebar.markdown("Clinical + Compliance + Recall Intelligence")
st.sidebar.markdown("---")
st.sidebar.markdown("**Documents Used:**")
st.sidebar.markdown("- FDA Dexcom Recall")
st.sidebar.markdown("- HIPAA Privacy Guidance")
st.sidebar.markdown("- WHO Diabetes Guideline")
st.sidebar.markdown("---")
st.sidebar.markdown("**Tech Stack:**")
st.sidebar.markdown("- Python")
st.sidebar.markdown("- LangChain")
st.sidebar.markdown("- ChromaDB")
st.sidebar.markdown("- Sentence Transformers")
st.sidebar.markdown("- Ollama / Llama 3.2")
st.sidebar.markdown("- Streamlit")


st.title("🏥 Healthcare RAG Assistant")
st.markdown(
    """
    A Retrieval-Augmented Generation application that answers questions from
    healthcare documents using local embeddings, ChromaDB, and a local LLM.
    """
)

tab1, tab2, tab3, tab4 = st.tabs(
    ["📌 Overview", "💬 Ask Assistant", "📄 Source Documents", "🧠 RAG Architecture"]
)


with tab1:
    st.header("Project Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Documents", "3")
    col2.metric("Pages Loaded", "45")
    col3.metric("Text Chunks", "85")
    col4.metric("Cost", "$0")

    st.subheader("Business Problem")
    st.write(
        """
        Healthcare teams often need to search across clinical guidelines,
        regulatory recall notices, and compliance documents. Manual review is
        time-consuming and can make it difficult to quickly locate relevant information.
        """
    )

    st.subheader("Solution")
    st.write(
        """
        This application uses Retrieval-Augmented Generation to retrieve relevant
        document sections and generate grounded answers based only on uploaded
        healthcare documents.
        """
    )

    st.subheader("Use Cases")
    st.markdown(
        """
        - Answer HIPAA compliance questions
        - Search FDA recall information
        - Summarize WHO diabetes guideline recommendations
        - Support healthcare document review and regulatory research
        """
    )


with tab2:
    st.header("Ask the Healthcare Assistant")

    sample_question = st.selectbox(
        "Choose a sample question or type your own below:",
        [
            "",
            "What does HIPAA say about breach notification?",
            "Why were Dexcom G7 sensors recalled?",
            "What are the goals of diabetes management?",
            "What are the key patient safety risks mentioned in the documents?",
            "What does the WHO guideline say about self-monitoring?"
        ]
    )

    user_question = st.text_input(
        "Enter your question:",
        value=sample_question
    )

    k = st.slider(
        "Number of source chunks to retrieve:",
        min_value=1,
        max_value=5,
        value=3
    )

    if st.button("Generate Answer"):
        if user_question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Retrieving relevant documents and generating answer..."):
                answer, sources = generate_answer(user_question, k=k)

            st.subheader("Answer")
            st.success(answer)

            st.subheader("Sources Used")

            for i, doc in enumerate(sources, start=1):
                with st.expander(f"Source {i}"):
                    st.write("Metadata:")
                    st.json(doc.metadata)

                    st.write("Retrieved Text:")
                    st.write(doc.page_content[:1200])


with tab3:
    st.header("Source Documents")

    st.write(
        """
        The RAG system currently uses three healthcare documents covering
        clinical guidance, compliance, and regulatory safety.
        """
    )

    docs = [
        {
            "Document": "FDA Dexcom Recall",
            "Domain": "Regulatory / Medical Device Recall",
            "Purpose": "Identify recall reasons, safety risks, affected products, and recommended actions."
        },
        {
            "Document": "HIPAA Privacy Guidance",
            "Domain": "Healthcare Compliance / Privacy",
            "Purpose": "Answer questions about PHI, Privacy Rule, Security Rule, and breach notification."
        },
        {
            "Document": "WHO Diabetes Guideline",
            "Domain": "Clinical Guideline",
            "Purpose": "Retrieve diabetes management recommendations, diagnosis guidance, and care principles."
        }
    ]

    st.dataframe(docs, use_container_width=True)

    st.subheader("Why these documents were selected")
    st.write(
        """
        These documents demonstrate a broad healthcare knowledge base:
        clinical care, regulatory operations, privacy compliance, and patient safety.
        This makes the project stronger than using only one document type.
        """
    )


with tab4:
    st.header("RAG Architecture")

    st.markdown(
        """
        ```text
        Healthcare PDFs
              ↓
        PDF Document Loader
              ↓
        Text Splitting / Chunking
              ↓
        Sentence Transformer Embeddings
              ↓
        ChromaDB Vector Database
              ↓
        Similarity Search Retriever
              ↓
        Ollama / Llama 3.2
              ↓
        Grounded Healthcare Answer
        ```
        """
    )

    st.subheader("Technology Stack")

    st.markdown(
        """
        - **Python**: Core programming language
        - **LangChain**: Document loading, chunking, vector retrieval workflow
        - **Sentence Transformers**: Free local embedding model
        - **ChromaDB**: Local vector database
        - **Ollama / Llama 3.2**: Local LLM for answer generation
        - **Streamlit**: Interactive web application
        """
    )

    st.subheader("RAG Safety Design")

    st.markdown(
        """
        The assistant is instructed to answer only from retrieved context.
        If information is not found in the uploaded documents, it should say
        that the answer was not found instead of guessing.
        """
    )