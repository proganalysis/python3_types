from flask_restplus import Namespace as Namespace
from typing import Any

AUTHORIZATION_URI: str
TOKEN_URI: str
USER_PROFILE_URI: str
SCOPE: Any
client_id: Any
client_secret: Any
redirect_uri: Any

def get_user_info(google_session: object) -> Any: ...
def register_google_oauth(namespace: Namespace) -> Any: ...
