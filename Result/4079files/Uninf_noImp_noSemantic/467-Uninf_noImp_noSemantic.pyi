from typing import Any

FROM_EMAIL: str
FROM_PWD: Any
SMTP_SERVER: str
SMTP_PORT: int
detach_dir: str

def get_body(email_message: Any): ...
def two_way_email(server: Any, uname: Any, pwd: Any) -> None: ...
