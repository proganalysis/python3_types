# (generated with --quick)

from typing import Any, List, TypeVar, Union

QApplication: Any
QPushButton: Any
ScrollGroup: Any

_T0 = TypeVar('_T0')

class TabRecent(Any):
    __doc__: str
    parent: Any
    recent_buttons: list
    recent_emoji: list
    def __init__(self, parent = ..., *args, **kwargs) -> None: ...
    def recentify(self, emote: _T0) -> List[Union[str, _T0]]: ...
