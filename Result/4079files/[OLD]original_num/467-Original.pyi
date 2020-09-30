# (generated with --quick)

from typing import Any

FROM_EMAIL: str
FROM_PWD: str
SMTP_PORT: int
SMTP_SERVER: str
detach_dir: str
email: module
html2text: Any
imaplib: module
os: module
sys: module
time: module

def get_body(email_message) -> Any: ...
def two_way_email(server, uname, pwd) -> None: ...
