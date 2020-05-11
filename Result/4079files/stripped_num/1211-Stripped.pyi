# (generated with --quick)

from typing import Any, Generator

LRUCache: Any

class LazyFastaContig:
    __doc__: str
    block_size: Any
    cache: Any
    contig: Any
    fasta: Any
    reference_length: Any
    def __getitem__(self, index) -> str: ...
    def __init__(self, fasta, contig, block_size = ..., cache_size = ...) -> None: ...
    def __len__(self) -> Any: ...
    def _get_block(self, block_index) -> Any: ...
    def _get_blocks(self, index) -> Generator[Any, Any, None]: ...
