# (generated with --quick)

import email.mime.multipart
import email.mime.text
from typing import Any, Optional, Tuple, Type

MIMEMultipart: Type[email.mime.multipart.MIMEMultipart]
MIMEText: Type[email.mime.text.MIMEText]
codecs: module
config: Any
emailer: EmailService
html2text: Any
smtplib: module

class EmailService(object):
    __doc__: str
    msg: email.mime.multipart.MIMEMultipart
    @staticmethod
    def attempt_login() -> Tuple[bool, Optional[smtplib.SMTP_SSL]]: ...
    def format_and_send_email(self, text, html, server) -> None: ...
    @staticmethod
    def load_newsletter_html() -> Tuple[Any, str]: ...
    def main(self) -> None: ...
