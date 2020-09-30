# (generated with --quick)

from typing import Any

DisplayName: Any
GetImage: Any
Image: module
Message: Any
asyncio: module
commands: Any
discord: Any
os: module
time: module

class Jpeg(Any):
    bot: Any
    jpeg: Any
    settings: Any
    def __init__(self, bot, settings) -> None: ...
    def _jpeg(self, image, compression = ...) -> bool: ...
    def _remove_transparency(self, image, fill_color = ...) -> Any: ...
    def canDisplay(self, server) -> bool: ...

def setup(bot) -> None: ...
