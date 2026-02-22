from typing import List


def grade_documents(query: str, documents: List[str]) -> List[str]:
    """
    Simple relevance filter (placeholder grading).
    Keeps documents that contain query keywords.
    """

    query_terms = query.lower().split()
    relevant_docs = []

    for doc in documents:
        if any(term in doc.lower() for term in query_terms):
            relevant_docs.append(doc)

    return relevant_docs