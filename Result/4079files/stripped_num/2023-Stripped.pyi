# (generated with --quick)

from typing import Any, Coroutine, List

Battle: Any
battlelog_parsing: Any
battles: list
formats: List[str]
log_in: Any
nb_fights: int
nb_fights_max: int
nb_fights_simu_max: int
senders: Any

def battle_tag(websocket, message, usage) -> Coroutine[Any, Any, None]: ...
def check_battle(battle_list, battletag) -> Any: ...
def stringing(websocket, message, usage = ...) -> Coroutine[Any, Any, None]: ...
