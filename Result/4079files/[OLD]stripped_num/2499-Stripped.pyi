# (generated with --quick)

from typing import Any, Dict, List, Tuple

Action: Any
HX2262Compatible: Any

class AB440S(Any):
    _h: str
    _l: str
    _off: List[str]
    _on: List[str]
    _repetitions: int
    def __init__(self) -> None: ...
    def get_bit_data(self, action) -> Tuple[list, int]: ...
    def get_channel_config_args(self) -> Dict[str, str]: ...
    def get_supported_actions(self) -> list: ...
