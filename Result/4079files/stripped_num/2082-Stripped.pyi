# (generated with --quick)

import functools
from typing import Any, Callable, Generator, Type, TypeVar

__author__: str
app: Any
attr: Any
bias_engine: Any
geometry: Any
logging: module
math: module
ncmc_switching: Any
np: module
openmm: Any
os: module
partial: Type[functools.partial]
perses: Any
sys: module
t: functools.partial[nothing]
test_testsystems_advanced: Any
test_valence: Callable
topology_proposal: Any
unit: Any

_FT = TypeVar('_FT', bound=Callable)

def run_samplers(testsystem_names, niterations = ...) -> Generator[functools.partial[nothing], Any, None]: ...
def skipIf(condition: object, reason: str) -> Callable[[_FT], _FT]: ...
def test_hybrid_scheme() -> Generator[functools.partial[nothing], Any, None]: ...
def test_testsystems_travis() -> None: ...
