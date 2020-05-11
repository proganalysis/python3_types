# (generated with --quick)

import multiprocessing.context
from typing import Any, List, Type

Process: Type[multiprocessing.context.Process]
hdlib: Any
i: str
inst: WasmProcess
mvar: Any
test_prgs: List[str]
wasm: Any

class WasmProcess:
    backend: Any
    instance: Any
    prg: Any
    thr: multiprocessing.context.Process
    def __init__(self, prg, backend = ..., platform = ...) -> None: ...
    def __str__(self) -> None: ...
    def from_json(self) -> None: ...
    def get_mem_block(self, block, size) -> Any: ...
    def get_self_diag(self) -> str: ...
    def run_script(self, params = ...) -> multiprocessing.context.Process: ...
