"""Utilities for loading PDF documents."""

from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


@dataclass
class PDFDocument:
    """Structured PDF extraction result."""

    file_name: str
    page_count: int
    text: str


def load_pdf_document(file_path: str) -> PDFDocument:
    """Extract text and metadata from a PDF file."""
    path = Path(file_path)
    reader = PdfReader(str(path))

    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")

    text = "\n".join(pages).strip()
    return PDFDocument(
        file_name=path.name,
        page_count=len(reader.pages),
        text=text,
    )


def load_pdf_text(file_path: str) -> str:
    """Extract text from a PDF file and return it as a single string."""
    return load_pdf_document(file_path).text
