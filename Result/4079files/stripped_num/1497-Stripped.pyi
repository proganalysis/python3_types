# (generated with --quick)

from typing import Any

Lego: Any

class TestingConnector(Any):
    temp_file: Any
    def __init__(self, baseplate, lock, temp_file = ...) -> None: ...
    def handle(self, message) -> None: ...
    @staticmethod
    def listening_for(message) -> bool: ...
