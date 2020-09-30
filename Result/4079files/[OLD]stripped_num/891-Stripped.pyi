# (generated with --quick)

import hashlib
from typing import Any, Union

base64: module
hmac: module
json: module
os: module
struct: module
time: module

def generate_confirmation_key(identity_secret, tag, timestamp = ...) -> bytes: ...
def generate_device_id(steam_id) -> str: ...
def generate_one_time_code(shared_secret, timestamp = ...) -> str: ...
def load_steam_guard(steam_guard) -> Any: ...
def sha1(__string: Union[bytearray, bytes, memoryview] = ...) -> hashlib._Hash: ...
