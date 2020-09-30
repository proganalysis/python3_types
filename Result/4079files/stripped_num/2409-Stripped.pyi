# (generated with --quick)

import cryptography.hazmat.primitives.ciphers
from typing import Any, Generator, Type

Cipher: Type[cryptography.hazmat.primitives.ciphers.Cipher]
_EMPTY_BLOCK: bytes
_PRINTABLE: str
algorithms: module
bcrypt: Any
itertools: module

def default_backend() -> Any: ...
def get_mask(n) -> int: ...
def get_password(kdf_rounds, character_set, length, increment, site_name, master_password) -> str: ...
def get_stream(key, nonce) -> Generator[nothing, Any, Any]: ...
