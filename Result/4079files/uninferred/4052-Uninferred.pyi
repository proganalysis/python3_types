from typing import Any, List, Tuple

class Interpretation:
    name: Any = ...
    parent: Any = ...
    children: Any = ...
    operations: Any = ...
    def __init__(self, name: str) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def pre(self) -> Tuple[Interpretation, ...]: ...

class Operation:
    name: Any = ...
    signatures: Any = ...
    def __init__(self, name: str) -> None: ...
    def __str__(self) -> str: ...
    def add_signature(self, interp: Interpretation, sig: Signature) -> None: ...
    def get_definition(self, interp: Interpretation) -> Interpretation: ...

class Signature:
    interpretation: Any = ...
    operation: Any = ...
    args: Any = ...
    result: Any = ...
    anchor: Any = ...
    def __init__(self, interpretation: Interpretation, operation: Operation, args: str, result: str, anchor: str) -> None: ...
    def with_result(self, new_result: str) -> Signature: ...
    def mdlink(self, ext: str=...) -> str: ...

class Specification:
    interpretations: Any = ...
    interpretations_byname: Any = ...
    operations: Any = ...
    operations_byname: Any = ...
    def __init__(self) -> None: ...
    def interpretations_pre(self) -> Tuple[Interpretation, ...]: ...
    def add_interpretation(self, interp: Interpretation) -> None: ...
    def get_operation(self, name: str) -> Operation: ...
    def extract_interpretations(self, text: str) -> None: ...
    def extract_operations(self, text: str) -> List[Tuple[Interpretation, Operation]]: ...
    def parse(self, text: str) -> None: ...
