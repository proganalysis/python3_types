from .colr import ColorArg as ColorArg, Colr
from .controls import Control
from typing import Optional

class ColrControl(Colr, Control):
    def __init__(self, text: Optional[str]=..., fore: Optional[ColorArg]=..., back: Optional[ColorArg]=..., style: Optional[str]=..., no_closing: Optional[bool]=...) -> None: ...
