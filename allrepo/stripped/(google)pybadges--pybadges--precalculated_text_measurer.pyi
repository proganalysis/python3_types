# (generated with --quick)

import pybadges.text_measurer
from typing import Any

io: module
json: module
pkg_resources: module
text_measurer: module

class PrecalculatedTextMeasurer(pybadges.text_measurer.TextMeasurer):
    __doc__: str
    _char_to_width: Any
    _default_cache: None
    _default_character_width: Any
    _pair_to_kern: Any
    def __init__(self, default_character_width, char_to_width, pair_to_kern) -> None: ...
    @classmethod
    def default(cls) -> Any: ...
    @staticmethod
    def from_json(f) -> PrecalculatedTextMeasurer: ...
    def text_width(self, text) -> Any: ...
