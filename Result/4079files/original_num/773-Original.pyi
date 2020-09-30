# (generated with --quick)

from typing import Any, Dict, Generator, List

FbxIOSettings: Any
FbxImporter: Any
FbxManager: Any
FbxScene: Any
curve: Dict[str, Any]
extractor: FbxCurvesExtractor
filename: str
layer: Any
stack: Any
ue: Any

class FbxCurvesExtractor:
    manager: Any
    scene: Any
    def __init__(self, filename) -> None: ...
    def get_anim_curves(self, layer) -> List[Dict[str, Any]]: ...
    def get_anim_layers(self, stack) -> list: ...
    def get_anim_stacks(self) -> list: ...
    def get_members_by_class(self, parent, name) -> list: ...
    def get_objects_by_class(self, name) -> list: ...
    def get_properties(self, obj) -> Generator[Any, Any, None]: ...
