# (generated with --quick)

from typing import Any, Generator

ALPHABETS: Any
AlphaEnum: Any
__init__: Any
fwd: str
strand: Strand
sys: module
uuid: module

class Strand:
    oligo: Any
    seq: Any
    strand3p: None
    strand5p: None
    uid: Any
    def __init__(self, seq, oligo, uid = ..., ctx = ...) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> Any: ...
    def gen3p(self) -> Generator[Strand, Any, None]: ...
    def gen5p(self) -> Generator[Strand, Any, None]: ...

def UnknownStrand(length) -> Strand: ...
