# (generated with --quick)

import asyncio.futures
from typing import Any, Optional

BLUE: Any
CYAN: Any
Color: Any
CustomObject: Any
CustomObjectMarkers: Any
CustomObjectTypes: Any
GREEN: Any
OFF: Any
PINK: Any
RED: Any
WHITE: Any
YELLOW: Any
asyncio: module
cozmo: Any
io: module
random: module

class VisionCube(Any):
    _chaser: Optional[asyncio.futures.Future]
    _color: Any
    _cube: Any
    def __init__(self, *a, **kw) -> None: ...
    def color(self) -> Any: ...
    def rainbow_chaser(self) -> None: ...
    def set_color(self, value) -> None: ...
    def start_light_chaser(self, value) -> None: ...
    def stop_light_chaser(self) -> None: ...
    def turn_of_lights(self) -> None: ...
