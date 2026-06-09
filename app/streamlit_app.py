"""Starter Streamlit application for the Enterprise AI Research Assistant."""

import streamlit as st


st.set_page_config(page_title="Enterprise AI Research Assistant", layout="wide")

st.title("Enterprise AI Research Assistant")
st.caption("Starter interface for a document-grounded research workflow.")

st.markdown(
    """
    This application will evolve into a retrieval-augmented research assistant that:

    - ingests enterprise PDF documents
    - indexes content for semantic search
    - retrieves relevant context for a question
    - generates grounded answers
    """
)

st.subheader("Project Status")
st.info("This is the initial repository scaffold. Core RAG functionality will be added incrementally.")

st.subheader("Planned Inputs")
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])
user_question = st.text_input("Ask a research question")

if uploaded_file:
    st.success(f"Selected file: {uploaded_file.name}")

if user_question:
    st.write("Question captured. Retrieval and answer generation will be connected in later iterations.")
