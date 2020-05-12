# (generated with --quick)

import cryptography.hazmat.primitives.ciphers
from typing import Any, Iterator, Sequence, Type

Cipher: Type[cryptography.hazmat.primitives.ciphers.Cipher]
_EMPTY_BLOCK: bytes
_PRINTABLE: str
algorithms: module
bcrypt: Any
itertools: module

def default_backend() -> Any: ...
def get_mask(n: int) -> int: ...
def get_password(kdf_rounds: int, character_set: Sequence[str], length: int, increment: int, site_name: str, master_password: str) -> str: ...
def get_stream(key: bytes, nonce: bytes) -> Iterator[int]: ...
