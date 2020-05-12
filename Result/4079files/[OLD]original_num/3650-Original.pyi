# (generated with --quick)

import pybadges.text_measurer
from typing import Mapping, TextIO

io: module
json: module
pkg_resources: module
text_measurer: module

class PrecalculatedTextMeasurer(pybadges.text_measurer.TextMeasurer):
    __doc__: str
    _char_to_width: Mapping[str, float]
    _default_cache: None
    _default_character_width: float
    _pair_to_kern: Mapping[str, float]
    def __init__(self, default_character_width: float, char_to_width: Mapping[str, float], pair_to_kern: Mapping[str, float]) -> None: ...
    @classmethod
    def default(cls) -> PrecalculatedTextMeasurer: ...
    @staticmethod
    def from_json(f: TextIO) -> PrecalculatedTextMeasurer: ...
