# (generated with --quick)

from typing import Any, Callable, List

Analyser_Osmosis: Any
sql10: str

class Analyser_Osmosis_Building_3nodes(Any):
    callback70: Callable[[Any], Any]
    requires_tables_diff: List[str]
    requires_tables_full: List[str]
    def __init__(self, config, logger = ...) -> None: ...
    def analyser_osmosis_diff(self) -> None: ...
    def analyser_osmosis_full(self) -> None: ...
