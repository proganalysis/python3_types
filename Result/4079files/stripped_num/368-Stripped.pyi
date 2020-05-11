# (generated with --quick)

import enum
from typing import Any, Callable, Type

BaldEagle: Any
Enum: Type[enum.Enum]
Interface: Type[implements.Interface]
MallardDuck: Any

class Animal:
    name: Any
    def __init__(self, name) -> None: ...

class Direction(enum.Enum):
    E: str
    N: str
    S: str
    W: str

class Flyable(implements.Interface):
    def fly(self) -> None: ...
    def migrate(self) -> None: ...

class Quackable(implements.Interface):
    echoes: None
    def quack(self) -> None: ...

def implements(interface_cls) -> Callable[[Any], Any]: ...
