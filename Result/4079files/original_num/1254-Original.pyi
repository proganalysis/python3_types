# (generated with --quick)

import collections
from typing import Any, Type

BinaryArithmeticOperation: Any
BinaryComparisonOperation: Any
BooleanLyraType: Any
Expression: Any
Input: Any
InputMixin: Any
IntegerLyraType: Any
JSONMixin: Any
Literal: Any
SignLattice: Any
SignState: Any
VariableIdentifier: Any
copy_docstring: Any
defaultdict: Type[collections.defaultdict]

class QuantityLattice(Any, Any):
    __doc__: str
    from_json: Any
    to_json: Any

class QuantityState(Any, Any):
    ExpressionRefinement: type
    __doc__: str
    _refinement: Any
    replace: Any
    unify: Any
    def __init__(self, variables: set, precursory = ...) -> None: ...
