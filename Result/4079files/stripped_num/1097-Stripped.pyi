# (generated with --quick)

from typing import Any, Coroutine, List

asyncio: module

class Menu:
    ChoiceSubmenu: type
    InputSubmenu: type
    Submenu: type
    __doc__: str
    children: List[nothing]
    main: Any
    def __init__(self, main_page) -> None: ...
    def add_child(self, child) -> None: ...
    def start(self, ctx) -> Coroutine[Any, Any, None]: ...
