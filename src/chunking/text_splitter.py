"""Helpers for splitting text into retrieval-ready chunks."""

from langchain.text_splitter import RecursiveCharacterTextSplitter


def build_text_splitter(chunk_size: int = 800, chunk_overlap: int = 100) -> RecursiveCharacterTextSplitter:
    """Create a default text splitter for PDF-derived content."""
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )


def split_text(text: str, chunk_size: int = 800, chunk_overlap: int = 100) -> list[str]:
    """Split raw text into chunks."""
    splitter = build_text_splitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)
