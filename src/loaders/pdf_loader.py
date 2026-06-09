"""Utilities for loading PDF documents."""

from pathlib import Path

from pypdf import PdfReader


def load_pdf_text(file_path: str) -> str:
    """Extract text from a PDF file and return it as a single string."""
    path = Path(file_path)
    reader = PdfReader(str(path))

    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")

    return "\n".join(pages).strip()
