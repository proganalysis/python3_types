from enot.compiler.abstract import AbstractCompiler
from typing import Any

class BootstrapCompiler(AbstractCompiler):
    def __init__(self, package: Any, executable: str = ...) -> None: ...
