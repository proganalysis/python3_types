# (generated with --quick)

import datetime
from typing import Any, List, Type, Union

GROUP_ID_SIZE: int
REFERENCE_DATE: datetime.date
SIGNATURE_SIZE: int
__all__: List[str]
base64: module
date: Type[datetime.date]
hashlib: module
hmac: module
settings: Any
struct: module
timezone: Any

def BASE64ENC(s: bytes) -> bytes: ...
def DIGESTMOD(__string: Union[bytearray, bytes, memoryview] = ...) -> hashlib._Hash: ...
def generate_code_for_group(group, expiration_date) -> Any: ...
def generate_date_fragment(expiration_date) -> Any: ...
def generate_msg_part_for_group(group, expiration_date) -> Any: ...
def get_next_promo_code(group) -> Any: ...
def is_promo_code_delayed() -> Any: ...
def next_promo_code_date() -> Any: ...
def sign_code(msg) -> Any: ...
