# (generated with --quick)

from typing import Any, Coroutine, Dict, List, Optional, Tuple, Type, TypeVar, Union

BrowserError: Any
ConfigFileWriter: Any
ET: module
KEYRING: Any
LOGIN_URL: Any
MFA_WAIT_METHODS: Any
NetworkError: Any
TimeoutError: Any
asyncio: module
base64: module
boto3: Any
datetime: Type[datetime.datetime]
getpass: module
json: module
keyring: module
launch: Any
os: module
time: module
uuid: module
zlib: module

AnyStr = TypeVar('AnyStr', str, bytes)

class FormError(Exception): ...

class Login:
    _AWAIT_TIMEOUT: int
    _BEGIN_AUTH_URL: str
    _CREDENTIALS: List[str]
    _END_AUTH_URL: str
    _EXEC_PATH: Optional[str]
    _MFA_DELAY: int
    _MFA_TIMEOUT: int
    _PROCESS_AUTH_URL: str
    _REFERER: str
    _RETRIES: int
    _SAML_REQUEST: Any
    _SAML_URL: str
    _SLEEP_TIMEOUT: int
    _account: Any
    _azure_app_id_uri: Any
    _azure_kmsi: Any
    _azure_mfa: Any
    _azure_password: None
    _azure_tenant_id: Any
    _azure_username: Any
    _config: Any
    _config_writer: Any
    _debug: Any
    _headless: Any
    _role: Any
    _session: Any
    _session_duration: int
    _use_keyring: Any
    saml_response: Any
    def __call__(self) -> int: ...
    def __init__(self, session, role = ..., account = ..., debug = ..., headless = ..., saml_request = ...) -> None: ...
    def _assume_role(self, role_arn, principal_arn, saml_response) -> Any: ...
    def _build_saml_login_url(self) -> str: ...
    @staticmethod
    def _choose_role(self, aws_roles) -> Tuple[Any, Any]: ...
    @staticmethod
    def _get_aws_roles(saml_response) -> list: ...
    def _login(self) -> int: ...
    @staticmethod
    def _post(session, url, data, headers) -> Any: ...
    @classmethod
    def _querySelector(cls, page, element, retries = ...) -> coroutine: ...
    def _render_js_form(self, url, username, password, mfa = ...) -> Coroutine[Any, Any, None]: ...
    def _save_credentials(self, credentials, role_arn) -> None: ...
    def _set_config_value(self, key, value) -> None: ...

class MfaException(Exception): ...

def parse_qs(qs: Optional[AnyStr], keep_blank_values: bool = ..., strict_parsing: bool = ..., encoding: str = ..., errors: str = ...) -> Dict[AnyStr, List[AnyStr]]: ...
@overload
def quote(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
