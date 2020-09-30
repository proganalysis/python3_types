# (generated with --quick)

from typing import Any, Generator, Optional, Tuple

BLUE_BASE: Any
BLUE_FLAG: Any
Base: Any
BaseProtocol: Any
CTF_MODE: Any
Flag: Any
GREEN_BASE: Any
GREEN_FLAG: Any

class Team(object):
    base: Any
    color: Tuple[int, int, int]
    flag: Any
    id: int
    kills: Optional[int]
    name: Optional[str]
    other: None
    protocol: Any
    score: Optional[int]
    spectator: bool
    def __init__(self, team_id: int, name: str, color: Tuple[int, int, int], spectator: bool, protocol) -> None: ...
    def count(self) -> int: ...
    def get_entities(self) -> Generator[Any, Any, None]: ...
    def get_entity_location(self, entity_id: int) -> Tuple[int, int, int]: ...
    def get_players(self) -> None: ...
    def get_random_location(self, force_land: bool = ...) -> Tuple[int, int, int]: ...
    def initialize(self) -> None: ...
    def set_base(self) -> Any: ...
    def set_flag(self) -> Any: ...
