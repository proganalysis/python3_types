# (generated with --quick)

from typing import Any

random: module

class Creature:
    level: Any
    name: Any
    def __init__(self, name, the_level) -> None: ...
    def __repr__(self) -> str: ...
    def get_defensive_roll(self) -> Any: ...

class Dragon(Creature):
    breaths_fire: Any
    level: Any
    name: Any
    scaliness: Any
    def __init__(self, name, level, scaliness, breaths_fire) -> None: ...

class SmallAnimal(Creature):
    level: Any
    name: Any

class Wizard(Creature):
    level: Any
    name: Any
    def attack(self, creature) -> bool: ...
