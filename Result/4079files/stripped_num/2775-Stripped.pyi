# (generated with --quick)

import ctypes
from typing import Any, Tuple, Type

BaseWindow: Any
Keys: Any
c_int: Type[ctypes.c_int]
context: Any
moderngl: Any
sdl2: Any
version: Any

class Window(Any):
    __doc__: str
    buffer_height: Any
    buffer_width: Any
    context: Any
    ctx: Any
    fbo: Any
    frames: Any
    height: Any
    keys: Any
    tmp_size_x: ctypes.c_int
    tmp_size_y: ctypes.c_int
    width: Any
    window: Any
    window_closing: bool
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def get_library_version(self) -> Tuple[Any, Any, Any]: ...
    def process_events(self) -> None: ...
    def resize(self, width, height) -> None: ...
    def should_close(self) -> bool: ...
    def swap_buffers(self) -> None: ...
    def terminate(self) -> None: ...
    def use(self) -> None: ...
