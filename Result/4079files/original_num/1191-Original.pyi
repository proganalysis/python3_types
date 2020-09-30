# (generated with --quick)

from typing import Any

Entity: Any
Game: Any
Status: Any
Team: Any
Transaction: Any
models: Any
random: module
string: module
timedelta: Any
transaction: Any
validators: Any

class Token(Any):
    CONSONANTS: str
    LENGTH: int
    VOWELS: str
    _use_commit: Any
    code: Any
    entity: Any
    used_by: Any
    used_time: Any
    value: Any
    def __repr__(self) -> str: ...
    @staticmethod
    def generate_one(entity, amount = ...) -> Token: ...
    @staticmethod
    def get(code: str) -> Any: ...
    @staticmethod
    def randomcode() -> str: ...
    def use(self, team) -> Any: ...

class TokenUnusableException(Exception): ...
