# (generated with --quick)

from typing import Any, Dict, List, NoReturn

class Module(object):
    args: Any
    compile_definitions: List[nothing]
    compiler_parameters: List[str]
    include_directories: List[nothing]
    name: None
    symbol_registry: Dict[nothing, nothing]
    def __init__(self, args) -> None: ...
    def gather_files(self) -> NoReturn: ...
    def register_passes(self, passes) -> None: ...
