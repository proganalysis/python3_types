# (generated with --quick)

import logging
import requests.exceptions
import requests.sessions
from typing import Any, Optional, TextIO, Type

ConnectionError: Type[requests.exceptions.ConnectionError]
Cookie: Any
LOG: logging.Logger
Session: Type[requests.sessions.Session]

def dict_from_cookiejar(cj) -> Any: ...
def getLogger(name: Optional[str] = ...) -> logging.Logger: ...
def getpass(prompt: str = ..., stream: Optional[TextIO] = ...) -> str: ...
def login(email: str, password: str, prompt, quiet, no_download, **kwargs) -> None: ...
