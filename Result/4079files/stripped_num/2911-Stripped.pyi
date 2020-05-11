# (generated with --quick)

from typing import Any, Callable, Dict, List

MAX_ENTITIES: Any
_: int
amount: int
arguments: list
esper: Any
gc: module
label: str
lines: list
num: int
options: optparse.Values
optparse: module
parser: optparse.OptionParser
pickle: module
plt: Any
result: Dict[int, float]
result_min: float
result_times: List[float]
results: Dict[int, Dict[int, float]]
sys: module
time: module
world: Any
x: Any
y: Any

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

class Position:
    x: int
    y: int
    def __init__(self) -> None: ...

class Projectile:
    lifespan: int
    size: int
    def __init__(self) -> None: ...

class Velocity:
    x: int
    y: int
    def __init__(self) -> None: ...

def create_entities(number) -> None: ...
def single_comp_query(*args) -> Any: ...
def three_comp_query(*args) -> Any: ...
def time_query() -> float: ...
def timing(f) -> Callable: ...
def two_comp_query(*args) -> Any: ...
