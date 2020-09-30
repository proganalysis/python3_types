# (generated with --quick)

from typing import Any, Dict

ADDR_SPEC: str
ATEXT: str
ATOM: str
CCONTENT: str
CFWS: str
COMMENT: str
CRLF: str
CTEXT: str
DCONTENT: str
DNS: Any
DOMAIN: str
DOMAIN_LITERAL: str
DOT_ATOM: str
DOT_ATOM_TEXT: str
DTEXT: str
FWS: str
LOCAL_PART: str
MX_CHECK_CACHE: Dict[Any, bool]
MX_DNS_CACHE: Dict[str, Any]
NO_WS_CTL: str
QCONTENT: str
QTEXT: str
QUOTED_PAIR: str
QUOTED_STRING: str
ServerError: Any
VALID_ADDRESS_REGEXP: str
WSP: str
email: str
logging: module
mx: Any
re: module
result: Any
smtplib: module
socket: module
time: module
validate: Any

def get_mx_ip(hostname) -> Any: ...
def raw_input(prompt = ...) -> str: ...
def validate_email(email, check_mx = ..., verify = ..., debug = ..., sending_email = ..., smtp_timeout = ...) -> Any: ...
