# (generated with --quick)

import meeseeksdev.meeseeksbox.scopes
from typing import Any, Dict, Pattern, Type

ACCEPT_HEADER: str
ACCEPT_HEADER_KORA: str
ACCEPT_HEADER_SYMMETRA: str
API_COLLABORATORS_TEMPLATE: str
Permission: Type[meeseeksdev.meeseeksbox.scopes.Permission]
RELINK_RE: Pattern[str]
datetime: module
green: str
json: module
jwt: module
normal: str
re: module
red: str
requests: module
yellow: str

class Authenticator:
    _session_class: Type[Session]
    _token: None
    duration: int
    idmap: dict
    integration_id: Any
    personnal_account_name: Any
    personnal_account_token: Any
    rsadata: Any
    since: int
    def __init__(self, integration_id, rsadata, personnal_account_token, personnal_account_name) -> None: ...
    def _build_auth_id_mapping(self) -> None: ...
    def _integration_authenticated_request(self, method, url) -> Any: ...
    def list_installations(self) -> Any: ...
    def session(self, installation_id) -> Session: ...

class Session(Authenticator):
    _session_class: Type[Session]
    _token: Any
    duration: int
    idmap: Dict[nothing, nothing]
    installation_id: Any
    integration_id: Any
    personnal_account_name: Any
    personnal_account_token: Any
    rsadata: Any
    since: int
    def __init__(self, integration_id, rsadata, installation_id, personnal_account_token, personnal_account_name) -> None: ...
    def _get_permission(self, org, repo, username) -> Any: ...
    def create_issue(self, org: str, repo: str, title: str, body: str, *, labels = ..., assignees = ...) -> Any: ...
    def get_collaborator_list(self, org, repo) -> Any: ...
    def ghrequest(self, method, url, json = ..., *, override_accept_header = ..., raise_for_status = ...) -> Any: ...
    def has_permission(self, org, repo, username, level = ...) -> Any: ...
    def personal_request(self, method, url, json = ..., raise_for_status = ...) -> Any: ...
    def post_comment(self, comment_url, body) -> None: ...
    def regen_token(self) -> None: ...
    def token(self) -> Any: ...

def fix_comment_body(body, original_poster, original_url, original_org, original_repo) -> str: ...
def fix_issue_body(body, original_poster, original_repo, original_org, original_number, migration_requester) -> str: ...
