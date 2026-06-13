import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

import streamlit as st
from src.rag_pipeline import generate_answer

st.set_page_config(
    page_title="Healthcare RAG Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Healthcare RAG Assistant")

st.markdown("""
Ask questions about:

- FDA Recall Documents
- HIPAA Compliance Documents
- WHO Clinical Guidelines
""")

question = st.text_input(
    "Enter your healthcare question:"
)

if st.button("Get Answer"):

    if question:

        with st.spinner("Searching documents..."):

            answer, sources = generate_answer(question)

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Sources")

        for i, doc in enumerate(sources, start=1):

            st.markdown(
                f"### Source {i}"
            )

            st.write(doc.metadata)

            st.write(
                doc.page_content[:1000]
            )