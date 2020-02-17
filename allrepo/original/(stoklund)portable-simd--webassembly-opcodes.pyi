# (generated with --quick)

from typing import Dict, Iterable, List, TextIO, Tuple

f: TextIO
it: simdspec.Interpretation
name_map: Dict[str, str]
omitted: Tuple[str, str, str, str]
psig: simdspec.Signature
re: module
sigs: List[Tuple[str, simdspec.Signature]]
simdspec: module
spec: simdspec.Specification
str_psig: str
wasm: List[simdspec.Interpretation]
wsig: str

def add_v128_load_store() -> None: ...
def format_sig(name: str, sig: simdspec.Signature) -> str: ...
def print_toc() -> None: ...
def snake_case(n: str) -> str: ...
def wasm_sigs(it: simdspec.Interpretation) -> Iterable[Tuple[str, simdspec.Signature]]: ...
