# (generated with --quick)

import _ast
import io
import typed_ast.ast3
import typed_astunparse.printer
from typing import Any, List, Type, Union

Printer: Type[typed_astunparse.printer.Printer]
Unparser: Any
VERSION: Any
__all__: List[str]
__version__: Any
ast: module
cStringIO: Type[io.StringIO]
t: module
typed_ast: module

def dump(tree: Union[_ast.AST, typed_ast.ast3.AST], annotate_fields: bool = ..., include_attributes: bool = ...) -> str: ...
def unparse(tree: Union[_ast.AST, typed_ast.ast3.AST]) -> str: ...
