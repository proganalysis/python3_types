# (generated with --quick)

import requests.models
from typing import Dict, Optional, Tuple, Union

json: module
logging: module
requests: module

class Caller(object):
    __doc__: str
    baseurl: str
    headers: Dict[str, str]
    host: str
    http_auth: Tuple[str, str]
    logger: logging.Logger
    password: str
    port: int
    retries: int
    timeout: int
    url_prefix: str
    use_https: bool
    user: str
    validate_cert: bool
    def delete(self, url: str, parameters: Optional[dict] = ...) -> requests.models.Response: ...
    def get(self, url: str, parameters: Optional[dict] = ...) -> requests.models.Response: ...
    def post(self, url: str, data: Optional[Union[dict, list]] = ...) -> requests.models.Response: ...
    def test_connection(self) -> bool: ...

def sleep(secs: float) -> None: ...
