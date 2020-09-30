# (generated with --quick)

from typing import Any, Callable

Analyser_Osmosis: Any
sql10: str
sql30: str

class Analyser_Osmosis_Highway_Features(Any):
    callback10: Callable[[Any], Any]
    callback30: Callable[[Any], Any]
    def __init__(self, config, logger = ...) -> None: ...
    def analyser_osmosis_common(self) -> None: ...
    def analyser_osmosis_diff(self) -> None: ...
    def analyser_osmosis_full(self) -> None: ...
