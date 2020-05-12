from typing import Any, Optional

__location__: Any

class AddTag:
    tag_name: Any = ...
    mission_element: Any = ...
    tag_type: Any = ...
    def validate(self): ...
    def cancel_click(self, object: Any, data: Optional[Any] = ...) -> None: ...
    def ok_click(self, object: Any, data: Optional[Any] = ...) -> None: ...
    def window_destroy(self, obj: Any, data: Optional[Any] = ...) -> None: ...
    def mission_element_changed(self, object: Any, data: Optional[Any] = ...) -> None: ...
    tag_types: Any = ...
    def set_tag_types(self, types: Any) -> None: ...
    gladefile: Any = ...
    builder: Any = ...
    mission_element_combo: Any = ...
    tag_type_combo: Any = ...
    tag_name_entry: Any = ...
    elements: Any = ...
    window: Any = ...
    callback: Any = ...
    def __init__(self, callback: Any) -> None: ...
