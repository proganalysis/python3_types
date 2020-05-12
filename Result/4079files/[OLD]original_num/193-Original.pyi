# (generated with --quick)

import io
from typing import Any, Optional, Type

DFA: Any
DFAState: Any
StringIO: Type[io.StringIO]
str_list: Any

class DFASerializer(object):
    dfa: Any
    literalNames: Optional[list]
    symbolicNames: Optional[list]
    def __init__(self, dfa, literalNames: Optional[list] = ..., symbolicNames: Optional[list] = ...) -> None: ...
    def __str__(self) -> Optional[str]: ...
    def getEdgeLabel(self, i: int) -> Any: ...
    def getStateString(self, s) -> str: ...

class LexerDFASerializer(DFASerializer):
    dfa: Any
    literalNames: Optional[list]
    symbolicNames: Optional[list]
    def __init__(self, dfa) -> None: ...
    def getEdgeLabel(self, i: int) -> str: ...
