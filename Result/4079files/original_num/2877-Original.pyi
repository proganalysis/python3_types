# (generated with --quick)

import __future__
import requests.sessions
from typing import Any, Pattern

API_TOKEN_PATTERN: Pattern[str]
API_TOKEN_REGEX: str
BeautifulSoup: Any
URL_ADD: str
URL_CUSTOMIZE: str
URL_LIST: str
argparse: module
os: module
print_function: __future__._Feature
re: module
requests: module

def _argparse() -> argparse.Namespace: ...
def _fetch_api_token(session) -> str: ...
def _session(args) -> requests.sessions.Session: ...
def get_current_emoji_list(session) -> list: ...
def main() -> None: ...
def raw_input(prompt: str = ...) -> str: ...
def upload_emoji(session, emoji_name, filename) -> None: ...
