# (generated with --quick)

import requests.models
import requests.sessions
from typing import Any, Dict, Optional

BeautifulSoup: Any
base64: module
requests: module
rsa: Any
time: module

class Login(object):
    auth_resp: requests.models.Response
    encrypted_password: bytes
    loginReq: requests.sessions.Session
    loginSession: requests.sessions.Session
    openid_response: requests.models.Response
    parameters: Dict[str, Any]
    resp: Any
    response_html: str
    rsa_exponent: Optional[int]
    rsa_modulus: Optional[int]
    rsa_publickey: Any
    rsa_timestamp: Optional[int]
    session: requests.sessions.Session
    def __init__(self, username, password, shared_secret) -> None: ...
    def getInfo(self) -> requests.sessions.Session: ...
    def loginRequest(self, username, encrypted_password, shared_secret) -> requests.sessions.Session: ...
    @staticmethod
    def returnParameters(html) -> Dict[str, Any]: ...
    def rsa_params(self, username) -> Dict[str, int]: ...
    def start_backpack_session(self) -> None: ...

def generate_one_time_code(shared_secret, timestamp = ...) -> str: ...
