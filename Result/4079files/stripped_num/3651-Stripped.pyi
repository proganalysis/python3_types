# (generated with --quick)

from typing import Any, Callable

abc: module
functools: module
md_column: Any
typing: module

class And(BaseOperator):
    __doc__: str
    operators: list
    def __init__(self, *ops) -> None: ...
    def generate_sql(self, emitter) -> OperatorResponse: ...

class AscSorter(Sorter):
    cols: tuple
    sort_order: str

class BaseOperator(abc.ABC):
    __and__: Callable
    __doc__: str
    __or__: Callable
    __rand__: Callable
    __ror__: Callable
    @abstractmethod
    def generate_sql(self, emitter) -> Any: ...

class BasicSetter(BaseOperator, ColumnValueMixin):
    __doc__: str
    set_operator: Any
    def generate_sql(self, emitter) -> OperatorResponse: ...

class ColumnValueMixin(object):
    __doc__: str
    column: Any
    value: Any
    def __init__(self, column, value) -> None: ...

class ComparisonOp(ColumnValueMixin, BaseOperator):
    __doc__: str
    column: Any
    operator: None
    value: Any
    def generate_sql(self, emitter) -> OperatorResponse: ...

class DecrementSetter(BasicSetter):
    __doc__: str
    set_operator: str

class DescSorter(Sorter):
    cols: tuple
    sort_order: str

class Eq(ComparisonOp):
    __doc__: str
    column: Any
    operator: str
    value: Any

class Gt(ComparisonOp):
    __doc__: str
    column: Any
    operator: str
    value: Any

class Gte(ComparisonOp):
    __doc__: str
    column: Any
    operator: str
    value: Any

class HackyILike(BaseOperator, ColumnValueMixin):
    __doc__: str
    def generate_sql(self, emitter) -> OperatorResponse: ...

class ILike(ComparisonOp):
    __doc__: str
    column: Any
    operator: str
    value: Any

class In(BaseOperator, ColumnValueMixin):
    def generate_sql(self, emitter) -> OperatorResponse: ...

class IncrementSetter(BasicSetter):
    __doc__: str
    set_operator: str

class Like(ComparisonOp):
    __doc__: str
    column: Any
    operator: str
    value: Any

class Lt(ComparisonOp):
    __doc__: str
    column: Any
    operator: str
    value: Any

class Lte(ComparisonOp):
    __doc__: str
    column: Any
    operator: str
    value: Any

class NEq(ComparisonOp):
    __doc__: str
    column: Any
    operator: str
    value: Any

class OperatorResponse:
    __slots__ = ["parameters", "sql"]
    __doc__: str
    parameters: Any
    sql: Any
    def __init__(self, sql, parameters) -> None: ...

class Or(BaseOperator):
    __doc__: str
    operators: list
    def __init__(self, *ops) -> None: ...
    def generate_sql(self, emitter) -> OperatorResponse: ...

class Sorter(BaseOperator):
    __doc__: str
    cols: tuple
    sort_order: Any
    def __init__(self, *columns) -> None: ...
    def generate_sql(self, emitter) -> OperatorResponse: ...

class ValueSetter(BasicSetter):
    __doc__: str
    set_operator: str

def requires_bop(func) -> Callable: ...
