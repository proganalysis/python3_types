# (generated with --quick)

from typing import Any, Generator, Optional

ErrorNodeImpl: Any
INVALID_INTERVAL: Any
ParseTree: Any
ParseTreeListener: Any
RuleContext: Any
TerminalNode: Any
TerminalNodeImpl: Any
Token: Any

class InterpreterRuleContext(ParserRuleContext):
    children: None
    exception: None
    ruleIndex: int
    start: None
    stop: None
    def __init__(self, parent: ParserRuleContext, invokingStateNumber: int, ruleIndex: int) -> None: ...

class ParserRuleContext(Any):
    children: Optional[list]
    exception: None
    invokingState: Any
    parentCtx: Any
    start: Any
    stop: Any
    def __init__(self, parent: None = ..., invokingStateNumber: Optional[int] = ...) -> None: ...
    def addChild(self, child) -> Any: ...
    def addErrorNode(self, badToken) -> Any: ...
    def addTokenNode(self, token) -> Any: ...
    def copyFrom(self, ctx: None) -> None: ...
    def enterRule(self, listener) -> None: ...
    def exitRule(self, listener) -> None: ...
    def getChild(self, i: int, ttype: Optional[type] = ...) -> Any: ...
    def getChildCount(self) -> int: ...
    def getChildren(self, predicate = ...) -> Generator[Any, Any, None]: ...
    def getSourceInterval(self) -> Any: ...
    def getToken(self, ttype: int, i: int) -> Any: ...
    def getTokens(self, ttype: int) -> list: ...
    def getTypedRuleContext(self, ctxType: type, i: int) -> Any: ...
    def getTypedRuleContexts(self, ctxType: type) -> list: ...
    def removeLastChild(self) -> None: ...
