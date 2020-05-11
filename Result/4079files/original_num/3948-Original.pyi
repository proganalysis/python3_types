# (generated with --quick)

from typing import Any, Iterable, List, Optional, Tuple, Union

mitmproxy: Any
t: module

class MitmproxyExtendedOptions(Any):
    inject_js_error_detection: bool
    inject_js_error_detection_filter: str
    strip_headers: Union[List[nothing], Iterable[Tuple[str, str]]]
    def __init__(self, strip_headers: Optional[Iterable[Tuple[str, str]]] = ..., inject_js_error_detection: bool = ..., inject_js_error_detection_filter: str = ..., **kwargs) -> None: ...
