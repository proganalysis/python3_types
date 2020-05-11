# (generated with --quick)

from typing import Any, Coroutine, Dict, Tuple

DEFAULT_GOOGLE_URL: str
NoKeywordProvided: Any
aiohttp: Any
asyncio: module
get_request: Any
google_geos: Any
parse_html: Any
random_desktop_headers: Any

def build_google_url(geo, keyword, number) -> Any: ...
def google_gather_results(data) -> Coroutine[Any, Any, Dict[str, Any]]: ...
def unpack_data(data_dict) -> Tuple[Any, Any, Any, Any]: ...
