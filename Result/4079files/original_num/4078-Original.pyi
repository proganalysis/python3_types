# (generated with --quick)

import pathlib
import typing
from typing import List, Type

Iterable: Type[typing.Iterable]
Path: Type[pathlib.Path]

class ImageLoader:
    __doc__: str
    _font_names: List[str]
    _img_base_dir: pathlib.Path
    _img_count_global: int
    _img_count_per_font: List[int]
    def __init__(self, img_dir_path: str) -> None: ...
    def get_font_count(self) -> int: ...
    def get_font_names(self) -> list: ...
    def get_image_count(self) -> int: ...
    def get_img_count_for_font(self, font_name: str) -> int: ...
    def iterate_images_for_fontname(self, font_name: str) -> typing.Iterable: ...
