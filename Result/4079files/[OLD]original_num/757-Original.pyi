# (generated with --quick)

from typing import Any, Dict, TypeVar, Union

login: Any
parse: module
requests: module

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')

class Notifications:
    GET_TOKEN: str
    ITEM_ALERT: str
    _session: Any
    apikey: Any
    cookies: Dict[str, Any]
    token: Any
    def __init__(self, username, password, shared_secret, apikey = ...) -> None: ...
    def add_listing_alert(self, intent, type, item_raw_name, blanket = ..., craftable = ...) -> Any: ...
    @staticmethod
    def gen_headers(path: _T0, ref: _T1, method: _T2) -> Dict[str, Union[str, _T0, _T1, _T2]]: ...
    def remove_listing_alert(self, intent, item_name) -> Any: ...
