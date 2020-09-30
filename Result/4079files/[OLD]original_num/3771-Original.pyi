# (generated with --quick)

import decimal
from typing import Any, List, Type

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
    actual_coins: decimal.Decimal
    last_changed: datetime.datetime
    level: int
    points: decimal.Decimal
    potential_coins: decimal.Decimal
    user: Any
    def __eq__(self, o: object) -> bool: ...
    def __init__(self, user, level: int, points: decimal.Decimal, actual_coins: decimal.Decimal, potential_coins: decimal.Decimal, achievements: list, last_changed: datetime.datetime) -> None: ...
    def __ne__(self, o: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def _validate(self) -> None: ...
    def to_dict(self) -> dict: ...
