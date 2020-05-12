# (generated with --quick)

import hashlib
import http.client
from typing import Any, Optional, Tuple, Type, Union

ENROLL_HOSTS: Any
HTTPConnection: Type[http.client.HTTPConnection]
PATHS: Any
decrypt: Any
encrypt: Any
hmac: module
normalize_serial: Any
restore_code_to_bytes: Any
struct: module

class HTTPError(Exception):
    response: Any
    def __init__(self, msg, response) -> None: ...

def b32encode(s: bytes) -> bytes: ...
def enroll(data, host = ..., path = ...) -> bytes: ...
def get_server_response(data, host, path) -> bytes: ...
def get_time_offset(region = ..., path = ...) -> int: ...
def initiate_paper_restore(serial, host = ..., path = ...) -> bytes: ...
def request_new_serial(region = ..., model = ...) -> Tuple[Any, str]: ...
def restore(serial, restore_code) -> str: ...
def sha1(__string: Union[bytearray, bytes, memoryview] = ...) -> hashlib._Hash: ...
def time() -> float: ...
def token_bytes(nbytes: Optional[int] = ...) -> bytes: ...
def validate_paper_restore(data, host = ..., path = ...) -> bytes: ...
