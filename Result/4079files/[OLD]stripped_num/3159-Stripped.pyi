# (generated with --quick)

from typing import Any, Dict, Match, Optional

DEFAULT_HTTP_USER_AGENT: str
colorize: Any
core: Any
importlib: module
linebuf: Any
metadict: Any
os: module
re: module
sys: module

class Settings(Any):
    BACKDOOR: str
    BROWSER: str
    CACHE_SIZE: str
    EDITOR: str
    HTTP_USER_AGENT: str
    PASSKEY: str
    PAYLOAD_PREFIX: str
    PROXY: None
    REQ_DEFAULT_METHOD: str
    REQ_HEADER_PAYLOAD: str
    REQ_INTERVAL: str
    REQ_MAX_HEADERS: int
    REQ_MAX_HEADER_SIZE: str
    REQ_MAX_POST_SIZE: str
    REQ_POST_DATA: str
    REQ_ZLIB_TRY_LIMIT: str
    SAVEPATH: str
    TARGET: None
    TMPPATH: str
    VERBOSITY: bool
    __doc__: str
    _settings: Dict[str, module]
    def __init__(self) -> None: ...
    def __setitem__(self, name, value) -> Any: ...
    @staticmethod
    def _get_HTTP_header_info(name) -> str: ...
    @staticmethod
    def _isattr(name) -> Optional[Match[str]]: ...
    @staticmethod
    def _load_settings() -> Dict[str, module]: ...
    @staticmethod
    def _set_HTTP_header(value) -> str: ...
    @staticmethod
    def format_docstring(name, linebuf_type, desc) -> str: ...
