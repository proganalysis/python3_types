from . import aggregation
from typing import Any

class AuthorsPerFilePath(aggregation.AbstractAggregator):
    name: str = ...
    @classmethod
    def provides(cls): ...
    @classmethod
    def requires(cls): ...
    output_database: Any = ...
    input_database: Any = ...
    pipeline: Any = ...
    def __init__(self) -> None: ...

def main() -> None: ...