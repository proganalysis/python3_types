# (generated with --quick)

from typing import Any, List

json: module
random: module
time: module

class Recommend2:
    __doc__: str
    _like: Any
    _time: Any
    def __init__(self, limit_time) -> None: ...
    def learn(self, info) -> None: ...
    def load(self, filename) -> None: ...
    def result(self, test_set, number) -> List[int]: ...
    def save(self, filename) -> None: ...
