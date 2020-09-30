from typing import Any

def raw_input(prompt: str = ...): ...

ServerError: Any

class ServerError(Exception): ...

WSP: str
CRLF: str
NO_WS_CTL: str
QUOTED_PAIR: str
FWS: Any
CTEXT: Any
CCONTENT: Any
COMMENT: Any
CFWS: Any
ATEXT: str
ATOM: Any
DOT_ATOM_TEXT: Any
DOT_ATOM: Any
QTEXT: Any
QCONTENT: Any
QUOTED_STRING: Any
LOCAL_PART: Any
DTEXT: Any
DCONTENT: Any
DOMAIN_LITERAL: Any
DOMAIN: Any
ADDR_SPEC: Any
VALID_ADDRESS_REGEXP: Any
MX_DNS_CACHE: Any
MX_CHECK_CACHE: Any

def get_mx_ip(hostname: Any): ...
def validate_email(email: Any, check_mx: bool = ..., verify: bool = ..., debug: bool = ..., sending_email: str = ..., smtp_timeout: int = ...): ...
