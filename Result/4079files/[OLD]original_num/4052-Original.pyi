# (generated with --quick)

from typing import Dict, List, Tuple, TypeVar

re: module

_TSignature = TypeVar('_TSignature', bound=Signature)

class Interpretation(object):
    __doc__: str
    children: List[Interpretation]
    name: str
    operations: list
    parent: Interpretation
    def __init__(self, name: str) -> None: ...
    def pre(self) -> Tuple[Interpretation, ...]: ...

class Operation(object):
    __doc__: str
    name: str
    signatures: Dict[Interpretation, Signature]
    def __init__(self, name: str) -> None: ...
    def add_signature(self, interp: Interpretation, sig: Signature) -> None: ...
    def get_definition(self, interp: Interpretation) -> Interpretation: ...

class Signature(object):
    __doc__: str
    anchor: str
    args: str
    interpretation: Interpretation
    operation: Operation
    result: str
    def __init__(self, interpretation: Interpretation, operation: Operation, args: str, result: str, anchor: str) -> None: ...
    def mdlink(self, ext: str = ...) -> str: ...
    def with_result(self: _TSignature, new_result: str) -> _TSignature: ...

class Specification(object):
    __doc__: str
    interpretations: List[Interpretation]
    interpretations_byname: Dict[str, Interpretation]
    operations: List[Operation]
    operations_byname: Dict[str, Operation]
    def add_interpretation(self, interp: Interpretation) -> None: ...
    def extract_interpretations(self, text: str) -> None: ...
    def extract_operations(self, text: str) -> List[Tuple[Interpretation, Operation]]: ...
    def get_operation(self, name: str) -> Operation: ...
    def interpretations_pre(self) -> Tuple[Interpretation, ...]: ...
    def parse(self, text: str) -> None: ...
