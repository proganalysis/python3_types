# (generated with --quick)

from typing import Any, List, Type

_VALID_FIELDS: List[str]
datetime: Type[datetime.datetime]
fmt_datetime: Any

class ZenobaseEvent(dict):
    __doc__: str
    def __init__(self, data) -> None: ...
    def _check_timestamp(self) -> None: ...
    def clean_data(self) -> None: ...
