from .attack import AttackContext
from .injections import Injection
from typing import Any, Callable, List, NamedTuple, Union
from xpath import Expression as Expression

fs_func: Any
saxon_func: Any

class Feature(NamedTuple):
    name: str
    tests: List[Union[Expression, Callable]]

def test_oob(path: Any): ...

features: Any

async def detect_features(context: AttackContext, injector: Injection) -> List[Feature]: ...
