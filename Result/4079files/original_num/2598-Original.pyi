# (generated with --quick)

from typing import Any

Animation: Any
Builder: Any
Factory: Any
Hud: Any
Label: Any

class ActionStatusLabel(Any, Any):
    anim: Any
    color: Any
    font_size: Any
    key: Any
    outline_color: Any
    outline_width: Any
    text: Any
    def __init__(self, key = ..., **kwargs) -> None: ...
    def get_name(self = ...) -> str: ...
    def reset_animation(self) -> None: ...
    def start(self) -> None: ...
    def update(self, text = ..., **kwargs) -> None: ...
