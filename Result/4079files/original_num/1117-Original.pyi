# (generated with --quick)

import typing
from typing import Type

Counter: Type[typing.Counter]

class StatusRequestData:
    context: str
    description: str
    repository: str
    sha: str
    state: str
    url: str
    @staticmethod
    def is_valid_status_data(data: dict) -> bool: ...
