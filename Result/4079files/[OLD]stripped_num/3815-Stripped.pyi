# (generated with --quick)

import abc
from typing import Any, Callable, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
Expression: Any
LyraType: Any
VariableIdentifier: Any

_FuncT = TypeVar('_FuncT', bound=Callable)

class Assignment(Statement):
    __doc__: str
    _left: Any
    _pp: Any
    _right: Any
    left: Any
    right: Any
    def __init__(self, pp, left, right) -> None: ...
    def __repr__(self) -> str: ...

class Call(Statement):
    _arguments: Any
    _forloop: Any
    _name: Any
    _pp: Any
    _typ: Any
    arguments: Any
    forloop: Any
    name: Any
    typ: Any
    def __init__(self, pp, name, arguments, typ, forloop = ...) -> None: ...
    def __repr__(self) -> str: ...

class DictDisplayAccess(ExpressionAccess):
    __doc__: str
    _keys: Any
    _pp: Any
    _typ: Any
    _values: Any
    keys: Any
    values: Any
    def __init__(self, pp, typ, keys, values) -> None: ...
    def __repr__(self) -> str: ...

class ExpressionAccess(Statement):
    __doc__: str
    _pp: Any
    _typ: Any
    typ: Any
    def __init__(self, pp, typ) -> None: ...

class ListDisplayAccess(ExpressionAccess):
    __doc__: str
    _items: Any
    _pp: Any
    _typ: Any
    items: Any
    def __init__(self, pp, typ, items) -> None: ...
    def __repr__(self) -> str: ...

class LiteralEvaluation(Statement):
    __doc__: str
    _literal: Any
    _pp: Any
    literal: Any
    def __init__(self, pp, literal) -> None: ...
    def __repr__(self) -> str: ...

class ProgramPoint:
    _column: Any
    _line: Any
    column: Any
    line: Any
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, line, column) -> None: ...
    def __ne__(self, other) -> bool: ...
    def __repr__(self) -> str: ...

class Raise(Statement):
    _pp: Any
    def __repr__(self) -> str: ...

class SetDisplayAccess(ExpressionAccess):
    __doc__: str
    _items: Any
    _pp: Any
    _typ: Any
    items: Any
    def __init__(self, pp, typ, items) -> None: ...
    def __repr__(self) -> str: ...

class SlicingAccess(ExpressionAccess):
    __doc__: str
    _lower: Any
    _pp: Any
    _stride: Any
    _target: Any
    _typ: Any
    _upper: Any
    lower: Any
    stride: Any
    target: Any
    upper: Any
    def __init__(self, pp, typ, target, lower, upper = ..., stride = ...) -> None: ...
    def __repr__(self) -> str: ...

class Statement(metaclass=abc.ABCMeta):
    __doc__: str
    _pp: Any
    pp: Any
    def __init__(self, pp) -> None: ...
    @abstractmethod
    def __repr__(self) -> Any: ...

class SubscriptionAccess(ExpressionAccess):
    __doc__: str
    _key: Any
    _pp: Any
    _target: Any
    _typ: Any
    key: Any
    target: Any
    def __init__(self, pp, typ, target, key) -> None: ...
    def __repr__(self) -> str: ...

class TupleDisplayAccess(ExpressionAccess):
    __doc__: str
    _items: Any
    _pp: Any
    _typ: Any
    items: Any
    def __init__(self, pp, typ, items) -> None: ...
    def __repr__(self) -> str: ...

class VariableAccess(ExpressionAccess):
    __doc__: str
    _pp: Any
    _typ: Any
    _variable: Any
    variable: Any
    def __init__(self, pp, typ, variable) -> None: ...
    def __repr__(self) -> str: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
