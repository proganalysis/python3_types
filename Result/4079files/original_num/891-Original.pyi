# (generated with --quick)

import hashlib
from typing import Optional, Union

base64: module
hmac: module
json: module
os: module
struct: module
time: module

def generate_confirmation_key(identity_secret: str, tag: str, timestamp: int = ...) -> bytes: ...
def generate_device_id(steam_id: str) -> str: ...
def generate_one_time_code(shared_secret: str, timestamp: Optional[int] = ...) -> str: ...
def load_steam_guard(steam_guard: str) -> dict: ...
def sha1(__string: Union[bytearray, bytes, memoryview] = ...) -> hashlib._Hash: ...
