# (generated with --quick)

from typing import Any, Optional, Tuple, Union

BooleanProperty: Any
BoxLayout: Any
Factory: Any
ListProperty: Any
NumericProperty: Any
ObjectProperty: Any
OptionProperty: Any
StringProperty: Any
TextInput: Any
XBase: Any
XError: Any
XTextInput: Any
_: Any
__all__: Tuple[str, str, str]
__author__: str
metrics: Any
path: module

class XFileOpen(XFilePopup):
    BUTTON_OPEN: Any
    TXT_ERROR_SELECTION: Any
    __doc__: str
    buttons: Any
    selection: list
    title: Any
    def dismiss(self, *largs, **kwargs) -> Any: ...

class XFilePopup(Any):
    CTRL_NEW_FOLDER: str
    CTRL_VIEW_ICON: str
    CTRL_VIEW_LIST: str
    __doc__: str
    browser: Any
    dirselect: Any
    multiselect: Any
    path: Any
    selection: Any
    size_hint_x: Any
    size_hint_y: Any
    view_mode: Any
    def _create_dir(self, instance) -> Optional[bool]: ...
    def _ctrls_click(self, instance) -> None: ...
    def _ctrls_init(self) -> Any: ...
    def _filter_selection(self, folders = ..., files = ...) -> None: ...
    def _get_body(self) -> Any: ...

class XFileSave(XFilePopup):
    BUTTON_SAVE: Any
    TXT_ERROR_FILENAME: Any
    __doc__: str
    browser: Any
    buttons: Any
    filename: Any
    title: Any
    def dismiss(self, *largs, **kwargs) -> Any: ...
    def get_full_name(self) -> Any: ...
    def on_selection(self, *largs) -> None: ...

class XFolder(XFilePopup):
    BUTTON_SELECT: Any
    TXT_ERROR_SELECTION: Any
    __doc__: str
    buttons: Any
    dirselect: bool
    selection: list
    title: Any
    def __init__(self, **kwargs) -> None: ...
    def dismiss(self, *largs, **kwargs) -> Any: ...

def makedirs(name: Union[_PathLike, bytes, str], mode: int = ..., exist_ok: bool = ...) -> None: ...
