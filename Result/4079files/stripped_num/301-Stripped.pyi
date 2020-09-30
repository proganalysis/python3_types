# (generated with --quick)

from typing import Any, Dict, List, Tuple, TypeVar, Union

Provider: Any
Response: Any
list_to_commas: Any
one_or_more: Any
requests: Any

_T0 = TypeVar('_T0')

class PopcornNotify(Any):
    __doc__: str
    _required: Dict[str, List[str]]
    _schema: Dict[str, Union[str, Dict[str, Any]]]
    base_url: str
    name: str
    path_to_errors: Tuple[str]
    site_url: str
    def _prepare_data(self, data: _T0) -> _T0: ...
    def _send_notification(self, data) -> Any: ...
