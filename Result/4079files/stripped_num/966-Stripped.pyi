# (generated with --quick)

import iconpy
from typing import Any, Optional, Type

IconGenerator: Type[iconpy.IconGenerator]
Image: module
app: App
os: module
wx: Any

class App(Any):
    frame: Frame
    def OnInit(self) -> bool: ...

class Frame(Any):
    antialiasing_check: Any
    height_text: Any
    icon_generator: Optional[iconpy.IconGenerator]
    icon_image: Any
    iconset_btn: Any
    imageset_btn: Any
    input_text: Any
    m_staticText1: Any
    m_staticText11: Any
    m_staticText2: Any
    m_staticText4: Any
    m_staticText7: Any
    m_staticText8: Any
    m_staticText9: Any
    platform_choice: Any
    quality_slider: Any
    width_text: Any
    def __del__(self) -> None: ...
    def __init__(self, parent = ...) -> None: ...
    def construct_object(self, output_path) -> None: ...
    def export_iconset(self, event) -> None: ...
    def export_imageset(self, event) -> None: ...
    def text_on_change(self, event) -> None: ...

class ImageDrop(Any):
    window: Any
    def OnDropFiles(self, x, y, filenames) -> bool: ...
    def __init__(self, window) -> None: ...
