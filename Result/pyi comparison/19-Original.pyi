# (generated with --quick)

from typing import Any, Generator, Optional

ALPHABETS: Any
AlphaEnum: Any
__init__: Any
fwd: str
strand: Strand
sys: module
uuid: module

class Strand:
    oligo: Any
    seq: str
    strand3p: None
    strand5p: None
    uid: Any
    def __init__(self, seq: str, oligo, uid: Optional[str] = ..., ctx: Optional[dict] = ...) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def gen3p(self) -> Generator[Strand, None, None]: ...
    def gen5p(self) -> Generator[Strand, None, None]: ...

def UnknownStrand(length: int) -> Strand: ...
