# (generated with --quick)

import io
import typed_astunparse.printer
from typing import Any, List, Type

Printer: Type[typed_astunparse.printer.Printer]
Unparser: Any
VERSION: Any
__all__: List[str]
__version__: Any
ast: module
cStringIO: Type[io.StringIO]
t: module
typed_ast: module

def dump(tree, annotate_fields = ..., include_attributes = ...) -> str: ...
def unparse(tree) -> str: ...
