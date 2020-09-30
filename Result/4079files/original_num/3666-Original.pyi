# (generated with --quick)

from typing import Any, Dict, List, NoReturn, Optional, Tuple

Color: Any
arcade: Any

class ChoiceMenu(Menu):
    actions: Any
    border_size: int
    cancel_choice_idx: Any
    label_height: Any
    label_location_map: Dict[nothing, nothing]
    label_step_size: int
    label_width: Any
    labels: Any
    selected_action_index: int
    title: None
    title_label: None
    title_step_size: int
    window_stack: Any
    def __init__(self, choices, title, initial_choice_idx = ..., cancel_choice_idx = ..., **kwargs) -> None: ...

class ConfirmActionMenu(ChoiceMenu):
    actions: Any
    border_size: int
    cancel_choice_idx: None
    label_height: Any
    label_location_map: Dict[nothing, nothing]
    label_step_size: int
    label_width: Any
    labels: Any
    selected_action_index: int
    title: None
    title_label: None
    title_step_size: int
    window_stack: Any
    def __init__(self, title, action, **kwargs) -> None: ...

class HelpMenu(MessageBox):
    actions: Any
    border_size: int
    cancel_choice_idx: None
    label_height: Any
    label_location_map: Dict[nothing, nothing]
    label_step_size: int
    label_width: Any
    labels: Any
    selected_action_index: int
    title: None
    title_label: None
    title_step_size: int
    window_stack: Any
    def __init__(self, **kwargs) -> None: ...

class Menu(Window):
    actions: Any
    border_size: int
    label_height: Any
    label_location_map: Dict[Tuple[Any, Any], int]
    label_step_size: int
    label_width: Any
    labels: list
    selected_action_index: Any
    title: None
    title_label: None
    title_step_size: int
    window_stack: Any
    def __init__(self, actions, initial_selected_action_index = ..., **kwargs) -> None: ...
    def _find_label_for_location(self, x, y) -> None: ...
    def do_action(self) -> None: ...
    def draw(self) -> None: ...
    def get_size(self) -> Tuple[Any, Any]: ...

class MessageBox(ChoiceMenu):
    actions: Any
    border_size: int
    cancel_choice_idx: None
    label_height: Any
    label_location_map: Dict[nothing, nothing]
    label_step_size: int
    label_width: Any
    labels: Any
    selected_action_index: int
    title: None
    title_label: None
    title_step_size: int
    window_stack: Any
    def __init__(self, title, action = ..., **kwargs) -> None: ...

class Rectangle(object):
    __doc__: str
    vertex_list: Any
    def __init__(self, x1, y1, x2, y2, batch) -> None: ...

class TextInput(Window):
    __doc__: str
    batch: Any
    border_size: int
    caret: Any
    document: Any
    layout: Any
    rectangle: Rectangle
    text_height: Any
    text_width: Any
    title: None
    title_label: None
    title_step_size: int
    window_stack: Any
    def __init__(self, callback, **kwargs) -> None: ...
    def _draw_start_pos(self, x, y) -> None: ...
    def callback(self, _1) -> Any: ...
    def do_action(self) -> None: ...
    def draw(self) -> None: ...
    def get_size(self) -> Tuple[Any, Any]: ...

class Window:
    border_size: int
    title: Any
    title_label: Any
    title_step_size: int
    window_stack: Any
    def __init__(self, window_stack, title = ...) -> None: ...
    def close(self) -> None: ...
    def do_action(self) -> NoReturn: ...
    def draw(self) -> Any: ...
    def draw_background(self) -> NoReturn: ...
    def draw_title(self) -> NoReturn: ...
    def get_size(self) -> NoReturn: ...
    def on_key_escape(self) -> None: ...
    def on_mouse_motion(self, x, y) -> None: ...
    def on_mouse_press(self, x, y, button) -> None: ...
    def on_text(self, text) -> None: ...
    def on_text_motion(self, motion) -> None: ...
    def open(self) -> None: ...
    def switch_focus(self, relative = ...) -> None: ...

class WindowStack:
    stack: List[Window]
    def __init__(self) -> None: ...
    def do_action(self) -> NoReturn: ...
    def draw(self) -> None: ...
    def is_visible(self) -> bool: ...
    def on_key_escape(self) -> None: ...
    def on_mouse_motion(self, x, y) -> None: ...
    def on_mouse_press(self, x, y, button) -> None: ...
    def on_text(self, text) -> None: ...
    def on_text_motion(self, motion) -> None: ...
    def switch_focus(self, relative = ...) -> None: ...

def create_html_text(text: str, color, width: Optional[int] = ..., anchor_x = ..., anchor_y = ..., font_size: float = ..., font_name = ..., bold: bool = ..., italic: bool = ...) -> Any: ...
