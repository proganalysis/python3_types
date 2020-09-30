# (generated with --quick)

import requests.models
import requests.sessions
from typing import Any, Type

Session: Type[requests.sessions.Session]
TOKENS_DIR: str
datetime: Type[datetime.datetime]
json: module
os: module
requests: module
time: module
timedelta: Type[datetime.timedelta]

class OAuth2Session(requests.sessions.Session):
    _client_id: Any
    _client_secret: Any
    _expires_at: datetime.datetime
    _refresh_token: Any
    def __init__(self, client, credentials) -> None: ...
    def _get_access_token(self) -> None: ...
    def request(self, method, url, **kwargs) -> requests.models.Response: ...

def _get_oauth_token(client_id, client_secret, grant_type, extra = ...) -> Any: ...
def get_channel_credentials(config_id) -> Any: ...
def load_client_credentials(cred_file = ...) -> Any: ...
def obtain_user_code(client_id) -> Any: ...
def poll_for_authorization(client_id, client_secret, user_code_response) -> Any: ...
def tokens_file_for_id(project_id) -> str: ...
