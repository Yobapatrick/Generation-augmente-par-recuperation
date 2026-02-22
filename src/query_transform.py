def reformulate_query(query: str) -> str:
    """
    Simple query reformulation.
    In real CRAG this could call an LLM.
    """
    return f"Explique en détail : {query}"