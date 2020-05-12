# (generated with --quick)

from typing import Any, Generator, Optional

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
    color: Any
    flag: Any
    id: Any
    kills: Optional[int]
    name: Any
    other: None
    protocol: Any
    score: Optional[int]
    spectator: Any
    def __init__(self, team_id, name, color, spectator, protocol) -> None: ...
    def count(self) -> int: ...
    def get_entities(self) -> Generator[Any, Any, None]: ...
    def get_entity_location(self, entity_id) -> Any: ...
    def get_players(self) -> Generator[Any, Any, None]: ...
    def get_random_location(self, force_land = ...) -> Any: ...
    def initialize(self) -> None: ...
    def set_base(self) -> Any: ...
    def set_flag(self) -> Any: ...
