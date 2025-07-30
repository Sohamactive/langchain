"""Document extraction chains.

This module provides different strategies for extracting information from collections
of documents using LangGraph and modern language models.

Available Strategies:
- Iterative: Processes documents sequentially, refining results at each step
- Map-Reduce: Processes documents in parallel, then combines results
- Recursive: Hierarchical processing for documents
"""

from langchain.chains.documents.map_reduce import create_map_reduce_chain
from langchain.chains.documents.stuff import create_stuff_documents_chain

__al__ = [
    "create_iterative_extractor",
    "create_map_reduce_extractor",
]
