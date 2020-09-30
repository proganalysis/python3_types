# (generated with --quick)

from typing import Any, Tuple

Image: module
argparse: module
args: argparse.Namespace
icon_generator: IconGenerator
input_image: Any
json: module
length: Any
os: module
output_directory: Any
parser: argparse.ArgumentParser
target_size: Tuple[Any, Any]
width: Any

class IconGenerator:
    anti_alias: bool
    image: Any
    output: Any
    platform: Any
    quality: Any
    def __init__(self) -> None: ...
    def generate_icon(self) -> None: ...
    def generate_image_set(self, name, target_size) -> None: ...
    def resize_image(self, target_size_given, size, scale) -> str: ...
