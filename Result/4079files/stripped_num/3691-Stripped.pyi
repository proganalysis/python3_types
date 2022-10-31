# (generated with --quick)

import requests.sessions
from typing import Any, Dict, Type

GITHUB_ENDPOINT: str
Session: Type[requests.sessions.Session]
json: module

def create_session(headers) -> requests.sessions.Session: ...
def get_commit_sha(commit) -> Any: ...
def get_data(response) -> Any: ...
def get_labels(pull_request) -> list: ...
def get_last_commit(pull_request) -> Any: ...
def get_pull_request(repository) -> Any: ...
def get_pull_requests(repository) -> Any: ...
def get_repository(data) -> Any: ...
def get_repository_url(repository) -> Any: ...
def get_status(statuses, status_name) -> Any: ...
def get_statuses(commit) -> dict: ...
def make_headers(token) -> Dict[str, str]: ...
def perform_request(session, query) -> Any: ...