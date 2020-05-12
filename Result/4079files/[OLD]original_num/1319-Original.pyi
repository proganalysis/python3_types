# (generated with --quick)

import io
from typing import Any, Dict, Type
import urllib.request

AES: module
CONFIG_SCHEMA: Any
CONF_HOST: Any
CONF_NAME: Any
CONF_PASSWORD: Any
DEFAULT_NAME: str
DOMAIN: str
StringIO: Type[io.StringIO]
base64: module
binascii: module
cv: Any
json: module
logging: module
urllib: module
vol: Any

class BuderusBridge(object):
    BS: int
    INTERRUPT: str
    PAD: str
    _BuderusBridge__content_type: str
    _BuderusBridge__ua: str
    _host: Any
    _ids: Dict[nothing, nothing]
    _key: bytes
    logger: logging.Logger
    name: Any
    opener: urllib.request.OpenerDirector
    def __init__(self, name, host, password) -> None: ...
    def _decrypt(self, enc) -> bytes: ...
    def _encrypt(self, plain) -> bytes: ...
    def _get_data(self, path) -> bytes: ...
    def _get_json(self, data) -> Any: ...
    def _get_value(self, j) -> Any: ...
    def _json_encode(self, value) -> str: ...
    def _set_data(self, path, data) -> None: ...
    def _submit_data(self, path, data) -> None: ...

def setup(hass, config) -> bool: ...
