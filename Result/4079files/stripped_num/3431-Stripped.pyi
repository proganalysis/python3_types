# (generated with --quick)

from typing import Any, Dict, TypeVar, Union

login: module
parse: module
requests: module

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')

class Listings:
    BUY_LISTING: str
    GET_LISTINGS: str
    GET_MY_LISTINGS: str
    GET_TOKEN: str
    REMOVE_LISTING: str
    SELL_LISTING: str
    _session: Any
    apikey: Any
    cookies: Dict[str, Any]
    token: Any
    def __init__(self, username, password, shared_secret, apikey = ...) -> None: ...
    def _supply_data(self, metal, keys, details, offers, buyout, tradeoffer_url) -> Dict[str, Any]: ...
    def create_buy_listing(self, type, item, tradeoffers_url, metal, keys, craftable = ..., offers = ..., buyout = ..., details = ...) -> Any: ...
    def create_sell_listing(self, assetid, metal, keys, tradeoffer_url, offers = ..., buyout = ..., details = ...) -> Any: ...
    @staticmethod
    def gen_headers(path: _T0, ref: _T1) -> Dict[str, Union[str, _T0, _T1]]: ...
    def get_my_listings(self, item_names = ..., intent = ..., inactive = ...) -> Any: ...
    def remove_buy_listing(self, appid, steamid, obj_id) -> Any: ...
    def remove_sell_listing(self, appid, assetid, steamid) -> Any: ...
    def search_listings(self, item, item_names = ..., intent = ..., page_size = ..., fold = ..., steamid = ..., **kwargs) -> Any: ...
