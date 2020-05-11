# (generated with --quick)

from typing import Any

Battle: Any
BattleFormation: Any
WorldAdmin: Any
admin: Any
battle_tick: Any
battle_turn: Any
start_battle: Any

def start(modeladmin, request, queryset) -> None: ...
def tick_action(modeladmin, request, queryset) -> None: ...
def turn_action(modeladmin, request, queryset) -> None: ...
