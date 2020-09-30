# (generated with --quick)

import pathlib
import typing
from typing import Generator, List, Optional, Type

Iterable: Type[typing.Iterable]
Path: Type[pathlib.Path]

class ImageLoader:
    __doc__: str
    _font_names: List[str]
    _img_base_dir: Optional[pathlib.Path]
    _img_count_global: int
    _img_count_per_font: List[int]
    def __init__(self, img_dir_path) -> None: ...
    def get_font_count(self) -> int: ...
    def get_font_names(self) -> List[str]: ...
    def get_image_count(self) -> int: ...
    def get_img_count_for_font(self, font_name) -> Optional[int]: ...
    def iterate_images_for_fontname(self, font_name) -> Generator[pathlib.Path, None, None]: ...
