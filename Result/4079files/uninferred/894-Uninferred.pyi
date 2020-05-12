from ..mainmenu import AdminMenu
from menus import SimpleOption as SimpleOption, Text as Text
from typing import Any

__all__: str

class PlayerCommandsMenu(AdminMenu):
    caption: Any = ...
    needed_flag: str = ...
    @classmethod
    def menu(cls): ...
