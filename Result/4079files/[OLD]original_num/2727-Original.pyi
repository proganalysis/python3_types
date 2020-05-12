# (generated with --quick)

from typing import Optional, Type

ElementTree: module
SDLInterface: Type[SDLInterface.SDLInterface]

class InterfaceParser:
    begin_tag: str
    end_tag: str
    interface: Optional[SDLInterface.SDLInterface]
    def __init__(self, raw_string) -> None: ...
    def has_interface(self) -> bool: ...
