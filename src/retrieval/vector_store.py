"""FAISS vector store helpers."""

from langchain_community.vectorstores import FAISS


def build_vector_store(texts: list[str], embeddings) -> FAISS:
    """Create a FAISS vector store from text chunks."""
    return FAISS.from_texts(texts=texts, embedding=embeddings)


def search_vector_store(vector_store: FAISS, query: str, top_k: int = 4):
    """Run a similarity search against the vector store."""
    return vector_store.similarity_search(query, k=top_k)
