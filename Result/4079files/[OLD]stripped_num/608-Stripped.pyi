# (generated with --quick)

from typing import Any, Union

Operation: Any
SceneNode: Any

class TranslateOperation(Any):
    _node: Any
    _old_transformation: Any
    _set_position: Any
    _translation: Any
    def __init__(self, node, translation, set_position = ...) -> None: ...
    def __repr__(self) -> str: ...
    def mergeWith(self, other) -> Union[TranslateOperation, bool]: ...
    def redo(self) -> None: ...
    def undo(self) -> None: ...
