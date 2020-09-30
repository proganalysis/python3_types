# (generated with --quick)

from typing import Any, Callable, List

MAX_ENTITIES: Any
amount: int
arguments: list
averaged_results: List[nothing]
current_pass: int
current_run: List[float]
esper: Any
options: optparse.Values
optparse: module
parser: optparse.OptionParser
pyplot: Any
results: List[List[float]]
sys: module
time: module
world: Any

class Brain:
    smarts: int
    def __init__(self) -> None: ...

class Command:
    attack: bool
    defend: bool
    def __init__(self) -> None: ...

class Damageable:
    defense: int
    def __init__(self) -> None: ...

class Health:
    hp: int
    def __init__(self) -> None: ...

class MovementProcessor(Any):
    def __init__(self) -> None: ...
    def process(self) -> None: ...

class Position:
    x: Any
    y: Any
    def __init__(self, x = ..., y = ...) -> None: ...

class Projectile:
    lifespan: int
    size: int
    def __init__(self) -> None: ...

class Velocity:
    x: Any
    y: Any
    def __init__(self, x = ..., y = ...) -> None: ...

def create_entities(world, number) -> None: ...
def query_entities(*args) -> Any: ...
def timing(f) -> Callable: ...
