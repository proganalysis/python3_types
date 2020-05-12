from typing import Any

class IconGenerator:
    platform: str = ...
    quality: int = ...
    output: Any = ...
    anti_alias: bool = ...
    image: Any = ...
    def __init__(self) -> None: ...
    def generate_icon(self) -> None: ...
    def generate_image_set(self, name: str, target_size: Tuple[float, float]) -> Any: ...
    def resize_image(self, target_size_given: bool, size: Tuple[float, float], scale: float) -> str: ...
