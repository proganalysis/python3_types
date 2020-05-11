# (generated with --quick)

import abc
from typing import Any, Callable, List, Optional, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
Expression: Any
LyraType: Any
VariableIdentifier: Any

_FuncT = TypeVar('_FuncT', bound=Callable)

class Assignment(Statement):
    __doc__: str
    _left: ExpressionAccess
    _pp: ProgramPoint
    _right: Statement
    left: Any
    right: Any
    def __init__(self, pp: ProgramPoint, left: ExpressionAccess, right: Statement) -> None: ...
    def __repr__(self) -> str: ...

class Call(Statement):
    _arguments: List[Statement]
    _forloop: bool
    _name: str
    _pp: ProgramPoint
    _typ: Any
    arguments: Any
    forloop: Any
    name: Any
    typ: Any
    def __init__(self, pp: ProgramPoint, name: str, arguments: List[Statement], typ, forloop: bool = ...) -> None: ...
    def __repr__(self) -> str: ...

class DictDisplayAccess(ExpressionAccess):
    __doc__: str
    _keys: List[Statement]
    _pp: ProgramPoint
    _typ: Any
    _values: List[Statement]
    keys: Any
    values: Any
    def __init__(self, pp: ProgramPoint, typ, keys: List[Statement], values: List[Statement]) -> None: ...
    def __repr__(self) -> str: ...

class ExpressionAccess(Statement):
    __doc__: str
    _pp: ProgramPoint
    _typ: Any
    typ: Any
    def __init__(self, pp: ProgramPoint, typ) -> None: ...

class ListDisplayAccess(ExpressionAccess):
    __doc__: str
    _items: List[Statement]
    _pp: ProgramPoint
    _typ: Any
    items: Any
    def __init__(self, pp: ProgramPoint, typ, items: List[Statement]) -> None: ...
    def __repr__(self) -> str: ...

class LiteralEvaluation(Statement):
    __doc__: str
    _literal: Any
    _pp: ProgramPoint
    literal: Any
    def __init__(self, pp: ProgramPoint, literal) -> None: ...
    def __repr__(self) -> str: ...

class ProgramPoint:
    _column: int
    _line: int
    column: Any
    line: Any
    def __eq__(self, other: ProgramPoint) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, line: int, column: int) -> None: ...
    def __ne__(self, other: ProgramPoint) -> bool: ...
    def __repr__(self) -> str: ...

class Raise(Statement):
    _pp: ProgramPoint
    def __repr__(self) -> str: ...

class SetDisplayAccess(ExpressionAccess):
    __doc__: str
    _items: List[Statement]
    _pp: ProgramPoint
    _typ: Any
    items: Any
    def __init__(self, pp: ProgramPoint, typ, items: List[Statement]) -> None: ...
    def __repr__(self) -> str: ...

class SlicingAccess(ExpressionAccess):
    __doc__: str
    _lower: Statement
    _pp: ProgramPoint
    _stride: Optional[Statement]
    _target: Statement
    _typ: Any
    _upper: Optional[Statement]
    lower: Any
    stride: Any
    target: Any
    upper: Any
    def __init__(self, pp: ProgramPoint, typ, target: Statement, lower: Statement, upper: Optional[Statement] = ..., stride: Optional[Statement] = ...) -> None: ...
    def __repr__(self) -> str: ...

class Statement(metaclass=abc.ABCMeta):
    __doc__: str
    _pp: ProgramPoint
    pp: Any
    def __init__(self, pp: ProgramPoint) -> None: ...
    @abstractmethod
    def __repr__(self) -> Any: ...

class SubscriptionAccess(ExpressionAccess):
    __doc__: str
    _key: Statement
    _pp: ProgramPoint
    _target: Statement
    _typ: Any
    key: Any
    target: Any
    def __init__(self, pp: ProgramPoint, typ, target: Statement, key: Statement) -> None: ...
    def __repr__(self) -> str: ...

class TupleDisplayAccess(ExpressionAccess):
    __doc__: str
    _items: List[Statement]
    _pp: ProgramPoint
    _typ: Any
    items: Any
    def __init__(self, pp: ProgramPoint, typ, items: List[Statement]) -> None: ...
    def __repr__(self) -> str: ...

class VariableAccess(ExpressionAccess):
    __doc__: str
    _pp: ProgramPoint
    _typ: Any
    _variable: Any
    variable: Any
    def __init__(self, pp: ProgramPoint, typ, variable) -> None: ...
    def __repr__(self) -> str: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
