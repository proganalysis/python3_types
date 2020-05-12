# (generated with --quick)

from typing import Any, Coroutine, Dict, Tuple

DEFAULT_YANDEX_URL: str
aiohttp: Any
asyncio: module
get_request: Any
parse_html: Any
random_desktop_headers: Any
yandex_geos: Any

def __getattr__(name) -> Any: ...
def build_yandex_url(geo, keyword, number, lr) -> Any: ...
def unpack_data(data_dict) -> Tuple[Any, Any, Any, Any, Any]: ...
def yandex_gather_results(data) -> Coroutine[Any, Any, Dict[str, Any]]: ...
