from antlr4.error.ErrorListener import ErrorListener
from typing import Any

class TnsErrorListenerException(ErrorListener):
    def syntaxError(self, recognizer: Any, offendingSymbol: Any, line: Any, column: Any, msg: Any, e: Any) -> None: ...
