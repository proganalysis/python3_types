# (generated with --quick)

import cryptography.hazmat.primitives.ciphers.aead
from typing import Tuple, Type, TypeVar, Union

AESGCM: Type[cryptography.hazmat.primitives.ciphers.aead.AESGCM]
ciphertext: str
hashlib: module
os: module

_T1 = TypeVar('_T1')

def decrypt(passphrase, ciphertext) -> str: ...
def deriveKey(passphrase, salt: _T1 = ...) -> Tuple[bytes, Union[bytes, _T1]]: ...
def encrypt(passphrase, plaintext) -> str: ...
def hexlify(data: bytes) -> bytes: ...
def unhexlify(hexlify: Union[bytes, str]) -> bytes: ...
