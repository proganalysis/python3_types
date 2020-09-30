# (generated with --quick)

from typing import Any, Dict, Generator, List, TextIO, Tuple

f: TextIO
it: Any
name_map: Dict[str, str]
omitted: Tuple[str, str, str, str]
psig: Any
re: module
sigs: List[Tuple[str, Any]]
simdspec: module
spec: simdspec.Specification
str_psig: Any
wasm: list
wsig: str

def add_v128_load_store() -> None: ...
def format_sig(name, sig) -> str: ...
def print_toc() -> None: ...
def snake_case(n) -> str: ...
def wasm_sigs(it) -> Generator[Tuple[str, Any], Any, None]: ...
