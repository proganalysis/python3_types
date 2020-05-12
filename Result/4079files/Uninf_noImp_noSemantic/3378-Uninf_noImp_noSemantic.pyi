import expression as Exp
import statement as Stm
from typing import Any, List, Optional

class Break(BaseException): ...

class Return(BaseException):
    val: Any = ...
    def __init__(self, val: Any) -> None: ...

class RuntimeError(BaseException):
    lineno: Any = ...
    msg: Any = ...
    def __init__(self, lineno: Any, msg: Any) -> None: ...

class Environment:
    parent: Any = ...
    values: Any = ...
    def __init__(self, parent: Optional[Any] = ...) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __str__(self): ...
    def getAt(self, distance: int, name: str) -> Any: ...
    def setAt(self, distance: int, name: str, val: Any) -> Any: ...
    def declare(self, key: Any, value: Any) -> None: ...

class Interpreter:
    globals: Any = ...
    context: Any = ...
    locals: Any = ...
    def __init__(self) -> None: ...
    def enterScope(self) -> None: ...
    def exitScope(self) -> None: ...
    def resolve(self, exp: Exp, depth: int) -> Any: ...
    def lookUpVariable(self, name: str, exp: Exp) -> Any: ...
    def interpret(self, ast: List[Stm.Stm]) -> Any: ...
    def execute(self, stm: Stm.Stm) -> Any: ...
    def contextualExecute(self, stmts: List[Stm.Stm], ctx: Environment) -> Any: ...
    def visitStmVarDecl(self, stm: Stm.VarDecl) -> Any: ...
    def visitStmFunDecl(self, stm: Stm.FunDecl) -> Any: ...
    def visitStmBlock(self, stm: Stm.Block) -> Any: ...
    def visitStmIf(self, stm: Stm.If) -> Any: ...
    def visitStmWhile(self, stm: Stm.While) -> Any: ...
    def visitStmBreak(self, stm: Stm.Break) -> Any: ...
    def visitStmReturn(self, stm: Stm.Return) -> Any: ...
    def visitStmPrint(self, stm: Stm.Print) -> Any: ...
    def visitStmExp(self, stm: Stm.Exp) -> Any: ...
    def evaluate(self, exp: Exp.Exp) -> Any: ...
    def visitExpAssign(self, exp: Exp.Assign) -> Any: ...
    def visitExpBinary(self, exp: Exp.Binary) -> Any: ...
    def visitExpUnary(self, exp: Exp.Unary) -> Any: ...
    def visitExpCall(self, exp: Exp.Call) -> Any: ...
    def visitExpIdent(self, exp: Exp.Ident) -> Any: ...
    def visitExpLiteral(self, exp: Exp.Literal) -> Any: ...

def is_num(val: Any) -> bool: ...
def are_compat(op: Any, left: Any, right: Any) -> bool: ...
def is_truthy(val: Any) -> bool: ...
def stringify(val: Any) -> str: ...

class Function:
    params: Any = ...
    closure: Any = ...
    body: Any = ...
    def __init__(self, params: List[str], closure: Environment, body: Stm.Block) -> None: ...
    def call(self, intpr: Interpreter, args: List) -> Any: ...
