# (generated with --quick)

import onelogin_aws_cli.configuration
from typing import Any, Callable, Optional, Type

Device: Any
Section: Type[onelogin_aws_cli.configuration.Section]
getpass: module
keyring: module

class MFACredentials(object):
    __doc__: str
    _config: onelogin_aws_cli.configuration.Section
    _devices: list
    _otp: Optional[str]
    device: Any
    has_device: bool
    has_otp: bool
    otp: str
    def __init__(self, config: onelogin_aws_cli.configuration.Section) -> None: ...
    def prompt_token(self) -> None: ...
    def ready(self) -> bool: ...
    def reset(self) -> None: ...
    def select_device(self, devices: list) -> None: ...

class UserCredentials(object):
    SERVICE_NAME: str
    __doc__: str
    configuration: onelogin_aws_cli.configuration.Section
    has_password: bool
    password: Any
    username: Any
    def __init__(self, config: onelogin_aws_cli.configuration.Section) -> None: ...
    def _load_password_from_keychain(self) -> None: ...
    def _prompt_user_password(self) -> None: ...
    def _save_password_to_keychain(self) -> None: ...
    def load_credentials(self) -> None: ...
    def load_password(self) -> None: ...
    def load_username(self) -> None: ...

def user_choice(question: str, options: list, renderer: Callable[[Any], str] = ..., saved_choice: Optional[str] = ...) -> Any: ...