# (generated with --quick)

from typing import Any, Dict, List, Tuple, Union

config: Dict[str, Union[str, List[str]]]

class Transplant:
    area: Tuple[int, int]
    chests: Any
    dest: Tuple[int, int]
    dist: Tuple[int, int]
    header: Any
    i: int
    names: Any
    npcs: Any
    signs: Any
    source: Tuple[int, int]
    tiles: Any
    def __init__(self) -> None: ...
    def rec_chests(self, chests) -> None: ...
    def rec_header(self, header) -> None: ...
    def rec_npcs(self, npcs, names) -> None: ...
    def rec_signs(self, signs) -> None: ...
    def rec_tiles(self, tiles) -> None: ...
    def run(self) -> None: ...
