# Enterprise AI Research Assistant

A professional starter repository for an enterprise-focused AI research assistant built with Python, Streamlit, LangChain, FAISS, sentence-transformers, and PDF ingestion utilities.

## Project Overview

This project provides the foundation for an internal AI research assistant that can ingest organizational knowledge, index documents for semantic retrieval, and answer user questions with context-aware responses.

The initial version is intentionally lightweight. It focuses on establishing a clean repository structure, modular application design, and clear development direction for a retrieval-augmented generation (RAG) workflow.

## Problem Statement

Organizations often store valuable knowledge across PDF reports, policy documents, internal research, and operational manuals. That information is difficult to search efficiently using traditional keyword-based methods.

The goal of this project is to create a research assistant that can:

- Ingest enterprise documents such as PDFs
- Split content into retrieval-friendly chunks
- Generate embeddings for semantic search
- Store and query vectors using FAISS
- Answer natural language questions using retrieved context

This repository serves as the starter framework for that system.

## Architecture

The project follows a modular pipeline so each stage can evolve independently:

1. `Loaders`
   Read and extract text from source documents.
2. `Chunking`
   Split extracted text into manageable segments for retrieval.
3. `Embeddings`
   Convert chunks into vector representations using sentence-transformers.
4. `Retrieval`
   Store and search embeddings with FAISS.
5. `Generation`
   Pass retrieved context into a LangChain-powered question-answering flow.
6. `Evaluation`
   Measure retrieval and answer quality over time.
7. `Application Layer`
   Expose the workflow through a Streamlit user interface.

### High-Level Flow

`PDF files -> text extraction -> chunking -> embeddings -> FAISS index -> retrieval -> answer generation -> Streamlit UI`

## Tech Stack

- `Python`
- `Streamlit` for the user interface
- `LangChain` for orchestration
- `FAISS` for local vector search
- `sentence-transformers` for embeddings
- `pypdf` for PDF text extraction
- `python-dotenv` for environment variable management
- `pytest` for future testing

## Repository Structure

```text
enterprise-ai-research-assistant/
├── app/
│   └── streamlit_app.py
├── data/
├── docs/
├── notebooks/
├── src/
│   ├── chunking/
│   │   └── text_splitter.py
│   ├── embeddings/
│   │   └── embedder.py
│   ├── evaluation/
│   │   └── evaluate.py
│   ├── generation/
│   │   └── qa_chain.py
│   ├── loaders/
│   │   └── pdf_loader.py
│   └── retrieval/
│       └── vector_store.py
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Add environment variables to a local `.env` file if needed later.
4. Place sample PDFs in the `data/` directory.
5. Run the Streamlit app to begin iterative development.

Example commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Roadmap

### Phase 1: Foundation

- Establish repository structure
- Add PDF ingestion
- Add text chunking
- Add embedding generation
- Add FAISS vector indexing
- Add basic Streamlit interface

### Phase 2: Core RAG Workflow

- Connect retrieval to question answering
- Add configurable prompts
- Add source-aware response formatting
- Add support for multiple documents

### Phase 3: Quality and Reliability

- Add evaluation scripts and benchmark queries
- Improve chunking strategy
- Add metadata filtering
- Add better error handling and logging

### Phase 4: Enterprise Readiness

- Add user authentication
- Add document access controls
- Add document management workflows
- Add deployment and monitoring support

## Current Progress

- PDF ingestion is implemented in the Streamlit app
- Uploaded PDF files are saved temporarily for processing
- Text is extracted with `pypdf` through `src/loaders/pdf_loader.py`
- The app displays file name, page count, character count, and a text preview
- Advanced RAG features such as chunking, embeddings, retrieval, FAISS workflows, and LLM generation are intentionally not implemented yet

## Current Status

This repository is a clean starter scaffold. Advanced features are intentionally deferred so the project can grow in a structured, maintainable way.
