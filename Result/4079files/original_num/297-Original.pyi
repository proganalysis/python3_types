# (generated with --quick)

from typing import Any

config: Any
functools: module
tornado: Any
urllib_parse: module

class GitHubOAuth2Mixin(Any):
    _OAUTH_ACCESS_TOKEN_URL: str
    _OAUTH_AUTHORIZE_URL: str
    get_authenticated_user: Any
    @staticmethod
    def _on_access_token(future, response) -> None: ...
