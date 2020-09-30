# (generated with --quick)

from typing import Any, Coroutine, Dict, List

CURRENCIES: List[str]
asyncio: module
json: module
logging: module
urlopen: Any

def fetch_exchange_rates(chain_1209k: str = ..., loop = ...) -> Coroutine[Any, Any, Dict[str, dict]]: ...
def fetch_from_api(base_url: str, chain_1209k: str, loop = ...) -> Coroutine[Any, Any, Dict[str, Any]]: ...
def main() -> None: ...
