"""Starter utilities for question answering chains."""


def build_prompt(question: str, context: str) -> str:
    """Build a simple grounded prompt for later LLM integration."""
    return (
        "You are an enterprise AI research assistant.\n"
        "Answer the question using only the provided context.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{question}\n\n"
        "Answer:"
    )
