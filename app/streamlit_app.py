"""Streamlit application for PDF ingestion."""

import sys
from pathlib import Path
from tempfile import NamedTemporaryFile

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.loaders.pdf_loader import load_pdf_document


PREVIEW_CHARACTER_LIMIT = 1000


def save_uploaded_pdf(uploaded_file) -> Path:
    """Persist the uploaded PDF to a temporary file and return its path."""
    suffix = Path(uploaded_file.name).suffix or ".pdf"
    with NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        return Path(temp_file.name)


def render_pdf_details(file_name: str, page_count: int, character_count: int, preview_text: str) -> None:
    """Render extracted PDF details in the Streamlit UI."""
    st.subheader("PDF Summary")
    st.write(f"**File name:** {file_name}")
    st.write(f"**Total pages:** {page_count}")
    st.write(f"**Total characters:** {character_count}")

    st.subheader("Preview")
    st.text_area(
        "First 1000 characters",
        value=preview_text,
        height=320,
        disabled=True,
    )


def main() -> None:
    """Run the PDF ingestion app."""
    st.set_page_config(page_title="Enterprise AI Research Assistant", layout="wide")

    st.title("Enterprise AI Research Assistant")
    st.caption("Upload a PDF to extract and inspect its text content.")

    uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

    if not uploaded_file:
        st.info("Upload a PDF file to view its extracted text summary.")
        return

    temp_path = None
    try:
        temp_path = save_uploaded_pdf(uploaded_file)
        pdf_document = load_pdf_document(str(temp_path))
        preview_text = pdf_document.text[:PREVIEW_CHARACTER_LIMIT] or "No extractable text was found in this PDF."

        render_pdf_details(
            file_name=uploaded_file.name,
            page_count=pdf_document.page_count,
            character_count=len(pdf_document.text),
            preview_text=preview_text,
        )
    except Exception as exc:
        st.error(f"Unable to process the uploaded PDF: {exc}")
    finally:
        if temp_path and temp_path.exists():
            temp_path.unlink()


if __name__ == "__main__":
    main()
