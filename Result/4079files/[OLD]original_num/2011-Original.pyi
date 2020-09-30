# (generated with --quick)

import email.mime.text
from typing import Any, Type

MIMEText: Type[email.mime.text.MIMEText]
smtplib: module

class GmailHandler:
    __doc__: str
    gmail: Any
    password: Any
    def __init__(self, gmail, password) -> None: ...
    def send_mail(self, receivers, subject, text) -> None: ...
