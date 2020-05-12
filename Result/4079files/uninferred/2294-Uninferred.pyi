from typing import Any

class EntityBuilder:
    _model: Any = ...
    def __init__(self) -> None: ...
    def get_model(self): ...
    _entity: Any = ...
    def entity(self, type: Any, idx: Any): ...
    _current: Any = ...
    def attribute(self, name: Any): ...
    def relation(self, name: Any): ...
    def value(self, value: Any): ...
    def unknown(self, unknowns: Any): ...
    def null(self): ...

class TypeBuilder:
    _model: Any = ...
    def __init__(self) -> None: ...
    def get_model(self): ...
    _instance: Any = ...
    def entity(self, name: Any, file: Any, lnr: Any, *parents: Any): ...
    def attribute(self, name: Any, type: Any, file: Any, lnr: Any, multi: bool = ..., nullable: bool = ..., comment: str = ...): ...
    _relation: Any = ...
    def relation(self, name: Any, type: Any, file: Any, lnr: Any, multi: Any, reverse: str = ..., comment: str = ...): ...
    def source_annotate(self, value: Any): ...
    def target_annotate(self, value: Any): ...

LOGGER: Any

def test_basic_model_export(snippetcompiler: Any) -> None: ...
def test_null_relation_model_export(snippetcompiler: Any) -> None: ...
def test_unknown_relation_model_export(snippetcompiler: Any) -> None: ...
def test_complex_attributes_model_export(snippetcompiler: Any) -> None: ...
