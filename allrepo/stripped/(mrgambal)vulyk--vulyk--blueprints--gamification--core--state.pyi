# (generated with --quick)

import decimal
from typing import Any, Dict, List, Type

Decimal: Type[decimal.Decimal]
User: Any
__all__: List[str]
datetime: Type[datetime.datetime]

class InvalidUserStateException(BaseException):
    __doc__: str

class UserState:
    __slots__ = ["achievements", "actual_coins", "last_changed", "level", "points", "potential_coins", "user"]
    __doc__: str
    achievements: dict
    actual_coins: Any
    last_changed: Any
    level: Any
    points: Any
    potential_coins: Any
    user: Any
    def __eq__(self, o) -> Any: ...
    def __init__(self, user, level, points, actual_coins, potential_coins, achievements, last_changed) -> None: ...
    def __ne__(self, o) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def _validate(self) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
