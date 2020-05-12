import simdspec
from typing import Any, Iterable, Tuple

spec: Any

def add_v128_load_store() -> None: ...

wasm: Any

def print_toc() -> None: ...

name_map: Any
omitted: Any

def snake_case(n: str) -> str: ...
def format_sig(name: str, sig: simdspec.Signature) -> str: ...
def wasm_sigs(it: simdspec.Interpretation) -> Iterable[Tuple[str, simdspec.Signature]]: ...

sigs: Any
str_psig: Any
