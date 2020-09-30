# (generated with --quick)

import email.header
import email.message
import functools
from typing import Any, Callable, List, Optional, Tuple, TypeVar, Union

codecs: module
email: module
imaplib: module
re: module

_T = TypeVar('_T')

class MailMessage:
    __doc__: str
    _raw_flag_data: list
    _raw_uid_data: Any
    attachments: Any
    bcc: Any
    bcc_values: Any
    cc: Any
    cc_values: Any
    date: Any
    flags: Any
    from_: Any
    from_values: Any
    html: Any
    id: str
    obj: email.message.Message
    subject: Any
    text: Any
    to: Any
    to_values: Any
    uid: Any
    def __init__(self, message_id: str, fetch_data) -> None: ...
    @staticmethod
    def _get_message_data_parts(fetch_data) -> Tuple[Any, Any, list]: ...
    def _parse_addresses(self, value: str) -> tuple: ...

def decode_header(header: Union[str, email.header.Header]) -> List[Tuple[bytes, Optional[str]]]: ...
def decode_value(value, encoding) -> str: ...
def lru_cache(maxsize: Optional[int] = ..., typed: bool = ...) -> Callable[[Callable[..., _T]], functools._lru_cache_wrapper[_T]]: ...
def parse_email_address(value: str) -> dict: ...
