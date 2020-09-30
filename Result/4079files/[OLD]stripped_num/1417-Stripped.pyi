# (generated with --quick)

from typing import Any, Dict, List, Union

aggregation: Any

class AuthorsPerFilePath(Any):
    input_database: str
    name: str
    output_database: str
    pipeline: List[Dict[str, Union[str, Dict[str, Union[str, Dict[str, Dict[str, Union[str, Dict[str, List[str]]]]]]]]]]
    def __init__(self) -> None: ...
    @classmethod
    def provides(cls) -> str: ...
    @classmethod
    def requires(cls) -> str: ...

def main() -> None: ...
