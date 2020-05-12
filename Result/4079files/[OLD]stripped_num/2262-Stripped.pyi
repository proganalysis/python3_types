# (generated with --quick)

import collections
import types
from typing import Any, Callable, Dict, List, Optional, Tuple, Type

aiohttp: Any
async_timeout: Any
asyncio: module
custom_exceptions: Any
deque: Type[collections.deque]
json: module
ratelimit_key_queue_map: Dict[Any, collections.deque[float]]
ratelimit_key_time_map: Dict[Any, float]
time: module
url_parser: module

def _add_request_parameters(func) -> Callable: ...
def _get_float(data, default) -> float: ...
def _get_int(data, default) -> int: ...
def basic_request(loop, api_key, timeout_seconds, endpoint, *args, method = ..., handle_ratelimiting = ..., _cur_retry = ..., **kwargs) -> coroutine: ...
def exc_info() -> Tuple[Optional[Type[BaseException]], Optional[BaseException], Optional[types.TracebackType]]: ...
def format_exception(etype: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[types.TracebackType], limit: Optional[int] = ..., chain: bool = ...) -> List[str]: ...
def get_platforms(*args, api_key = ..., handle_ratelimiting = ..., timeout_seconds = ..., api_version = ..., loop = ..., **kwargs) -> coroutine: ...
def get_player(*args, api_key = ..., handle_ratelimiting = ..., timeout_seconds = ..., api_version = ..., loop = ..., **kwargs) -> coroutine: ...
def get_player_batch(*args, api_key = ..., handle_ratelimiting = ..., timeout_seconds = ..., api_version = ..., loop = ..., **kwargs) -> coroutine: ...
def get_playlists(*args, api_key = ..., handle_ratelimiting = ..., timeout_seconds = ..., api_version = ..., loop = ..., **kwargs) -> coroutine: ...
def get_ranked_leaderboard(*args, api_key = ..., handle_ratelimiting = ..., timeout_seconds = ..., api_version = ..., loop = ..., **kwargs) -> coroutine: ...
def get_seasons(*args, api_key = ..., handle_ratelimiting = ..., timeout_seconds = ..., api_version = ..., loop = ..., **kwargs) -> coroutine: ...
def get_stats_leaderboard(*args, api_key = ..., handle_ratelimiting = ..., timeout_seconds = ..., api_version = ..., loop = ..., **kwargs) -> coroutine: ...
def get_tiers(*args, api_key = ..., handle_ratelimiting = ..., timeout_seconds = ..., api_version = ..., loop = ..., **kwargs) -> coroutine: ...
def search_players(*args, api_key = ..., handle_ratelimiting = ..., timeout_seconds = ..., api_version = ..., loop = ..., **kwargs) -> coroutine: ...
