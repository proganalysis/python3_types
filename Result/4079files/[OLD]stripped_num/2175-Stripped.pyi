# (generated with --quick)

import decimal
import requests.sessions
from typing import Any, Callable, Type

ApiException: Any
ConfirmationExecutor: Any
Currency: Any
Decimal: Type[decimal.Decimal]
GameOptions: Any
LoginRequired: Any
Session: Type[requests.sessions.Session]
SteamUrl: Any
TooManyRequests: Any
get_listing_id_to_assets_address_from_html: Any
get_market_listings_from_html: Any
get_market_sell_listings_from_api: Any
json: module
merge_items_with_descriptions_from_listing: Any
text_between: Any

class SteamMarket:
    _session: Any
    _session_id: Any
    _steam_guard: Any
    was_login_executed: bool
    def __init__(self, session) -> None: ...
    def _confirm_sell_listing(self, asset_id) -> Any: ...
    def _set_login_executed(self, steamguard, session_id) -> None: ...
    def cancel_buy_order(self, *args, **kwargs) -> Any: ...
    def cancel_sell_order(self, *args, **kwargs) -> None: ...
    def create_buy_order(self, *args, **kwargs) -> Any: ...
    def create_sell_order(self, *args, **kwargs) -> Any: ...
    def fetch_price(self, item_hash_name, game, currency = ...) -> Any: ...
    def fetch_price_history(self, *args, **kwargs) -> Any: ...
    def get_my_market_listings(self, *args, **kwargs) -> Any: ...

def login_required(func) -> Callable: ...
