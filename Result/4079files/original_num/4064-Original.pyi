# (generated with --quick)

import email.message
import email.mime.base
import email.mime.multipart
import functools
from typing import Any, NoReturn, Optional, Set, Type

BasePlugin: Any
Buttons: Any
CloseButton: Any
EnterButton: Any
MIMEBase: Type[email.mime.base.MIMEBase]
MIMEMultipart: Type[email.mime.multipart.MIMEMultipart]
OkButton: Any
PaymentRequest: Any
PrintError: Any
QGridLayout: Any
QInputDialog: Any
QLabel: Any
QLineEdit: Any
QVBoxLayout: Any
WindowModalDialog: Any
_: Any
base64: module
email: module
get_parent_main_window: Any
hook: Any
imaplib: module
partial: Type[functools.partial]
random: module
smtplib: module
sys: module
threading: module
time: module
traceback: module

class CheckConnectionThread(Any):
    connection_error_signal: Any
    password: Any
    server: Any
    username: Any
    def __init__(self, server, username, password) -> None: ...
    def run(self) -> None: ...

class Plugin(Any):
    close_wallet: Any
    imap_server: Any
    load_wallet: Any
    obj: QEmailSignalObject
    password: Any
    pr: Any
    processor: Processor
    receive_list_menu: Any
    username: Any
    wallets: Set[nothing]
    def __init__(self, parent, config, name) -> None: ...
    def description(self) -> Any: ...
    def fullname(self) -> str: ...
    def is_available(self) -> bool: ...
    def new_invoice(self) -> None: ...
    def on_receive(self, pr_str) -> None: ...
    def requires_settings(self) -> bool: ...
    def send(self, window, addr) -> None: ...
    def settings_dialog(self, window) -> None: ...
    def settings_widget(self, window) -> Any: ...

class Processor(threading.Thread, Any):
    M: Optional[imaplib.IMAP4_SSL]
    connect_wait: int
    daemon: bool
    imap_server: Any
    on_receive: Any
    password: Any
    polling_interval: int
    username: Any
    def __init__(self, imap_server, username, password, callback) -> None: ...
    def poll(self) -> None: ...
    def reset_connect_wait(self) -> None: ...
    def run(self) -> NoReturn: ...
    def send(self, recipient, message, payment_request) -> None: ...

class QEmailSignalObject(Any):
    email_new_invoice_signal: Any

def __getattr__(name) -> Any: ...
def encode_base64(msg: email.message.Message) -> None: ...
