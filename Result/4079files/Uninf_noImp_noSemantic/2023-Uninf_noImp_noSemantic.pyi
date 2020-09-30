from typing import Any

battles: Any
nb_fights_max: int
nb_fights_simu_max: int
nb_fights: int
formats: Any

def check_battle(battle_list: Any, battletag: Any) -> None: ...
async def battle_tag(websocket: Any, message: Any, usage: Any) -> None: ...
async def stringing(websocket: Any, message: Any, usage: int = ...) -> None: ...
