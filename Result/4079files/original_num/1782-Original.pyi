# (generated with --quick)

import strand
from typing import Any, Optional, Type

ALPHABETS: Any
AlphaEnum: Any
Strand: Type[strand.Strand]
__init__: Any
sys: module

class Oligo(object):
    __doc__: str
    seq: Optional[str]
    strand5p: Optional[strand.Strand]
    def __init__(self, seq: Optional[str] = ...) -> None: ...
    def __len__(self) -> int: ...
    def prepend5p(self, strand: strand.Strand) -> None: ...
