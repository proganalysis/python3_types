from typing import Any

TIME_OUT: Any
INTERAL: Any
MAX_RETRIES: Any
EXCP_INTERAL: Any
COOKIES: Any

def is_banned(url: Any): ...
def get_page(url: Any, auth_level: int = ..., is_ajax: bool = ..., need_proxy: bool = ...): ...
