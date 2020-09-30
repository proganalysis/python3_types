# (generated with --quick)

from typing import Any, Dict, List, NoReturn, Tuple

Buffer: Any
Renderbuffer: Any
Texture: Any
__all__: List[str]

class Framebuffer:
    __slots__ = ["_color_attachments", "_depth_attachment", "_glo", "_samples", "_size", "ctx", "extra", "mglo"]
    __doc__: str
    _color_attachments: None
    _depth_attachment: None
    _glo: None
    _samples: None
    _size: Tuple[None, None]
    bits: Dict[str, str]
    color_attachments: tuple
    color_mask: Tuple[bool, bool, bool, bool]
    ctx: None
    depth_attachment: Any
    depth_mask: bool
    extra: None
    glo: int
    height: int
    mglo: None
    samples: int
    size: tuple
    viewport: Tuple[int, int, int, int]
    width: int
    def __eq__(self, other) -> bool: ...
    def __init__(self) -> NoReturn: ...
    def __repr__(self) -> str: ...
    def clear(self, red = ..., green = ..., blue = ..., alpha = ..., depth = ..., *, viewport = ...) -> None: ...
    def read(self, viewport = ..., components = ..., *, attachment = ..., alignment = ..., dtype = ...) -> bytes: ...
    def read_into(self, buffer, viewport = ..., components = ..., *, attachment = ..., alignment = ..., dtype = ..., write_offset = ...) -> None: ...
    def release(self) -> None: ...
    def use(self) -> None: ...
