# (generated with --quick)

from typing import Any, Coroutine, Dict, List

CURRENCIES: List[str]
asyncio: module
json: module
logging: module
urlopen: Any

def fetch_exchange_rates(chain_1209k = ..., loop = ...) -> Coroutine[Any, Any, Dict[str, Dict[str, Any]]]: ...
def fetch_from_api(base_url, chain_1209k, loop = ...) -> coroutine: ...
def main() -> None: ...
