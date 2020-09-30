# (generated with --quick)

from typing import Any

DefaultAccountAdapter: Any
DefaultSocialAccountAdapter: Any
HttpRequest: Any
settings: Any

class AccountAdapter(Any):
    def is_open_for_signup(self, request) -> Any: ...

class SocialAccountAdapter(Any):
    def is_open_for_signup(self, request, sociallogin) -> Any: ...
