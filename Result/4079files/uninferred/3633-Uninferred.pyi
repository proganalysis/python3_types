from persimmon.view.blocks.block import Block
from persimmon.view.pins import InputPin as InputPin, OutputPin as OutputPin
from typing import Any

class SVMBlock(Block):
    out_1: Any = ...
    def function(self) -> None: ...
