# (generated with --quick)

import io
from typing import Any, Optional, Type

DFA: Any
DFAState: Any
StringIO: Type[io.StringIO]
str_list: Any

class DFASerializer(object):
    dfa: Any
    literalNames: Any
    symbolicNames: Any
    def __init__(self, dfa, literalNames = ..., symbolicNames = ...) -> None: ...
    def __str__(self) -> Optional[str]: ...
    def getEdgeLabel(self, i) -> Any: ...
    def getStateString(self, s) -> str: ...

class LexerDFASerializer(DFASerializer):
    dfa: Any
    literalNames: None
    symbolicNames: None
    def __init__(self, dfa) -> None: ...
    def getEdgeLabel(self, i) -> str: ...
