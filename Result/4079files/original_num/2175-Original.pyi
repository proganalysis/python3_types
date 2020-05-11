# (generated with --quick)

import decimal
import requests.sessions
from typing import Any, Callable, Optional, Type

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
    _session: requests.sessions.Session
    _session_id: Optional[str]
    _steam_guard: Optional[dict]
    was_login_executed: bool
    def __init__(self, session: requests.sessions.Session) -> None: ...
    def _confirm_sell_listing(self, asset_id: str) -> dict: ...
    def _set_login_executed(self, steamguard: dict, session_id: str) -> None: ...
    def cancel_buy_order(self, *args, **kwargs) -> dict: ...
    def cancel_sell_order(self, *args, **kwargs) -> None: ...
    def create_buy_order(self, *args, **kwargs) -> dict: ...
    def create_sell_order(self, *args, **kwargs) -> dict: ...
    def fetch_price(self, item_hash_name: str, game, currency: str = ...) -> dict: ...
    def fetch_price_history(self, *args, **kwargs) -> dict: ...
    def get_my_market_listings(self, *args, **kwargs) -> dict: ...

def login_required(func) -> Callable: ...
