# (generated with --quick)

import dino_api
from typing import Any, Type

Board: Type[dino_api.Board]
Config: Any
neat: Any
nn: Any
os: module
pickle: module
population: Any

class GetCommand(object):
    net: Any
    def __call__(self, distance: int, size: int, speed: int) -> str: ...
    def __init__(self, net) -> None: ...

def eval_fitness(genomes: list, config) -> None: ...
def main() -> None: ...
