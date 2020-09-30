# (generated with --quick)

import framework
from typing import Any, Coroutine, Optional, Pattern, Type, TypeVar

Example: Type[framework.Example]
aiohttp: Any
aioxmpp: Any
argparse: module
asyncio: module
configparser: module
file_sender: Any
namespaces: Any
os: module
pathlib: module
re: module
subprocess: module
sys: module

_T1 = TypeVar('_T1')

class Upload(framework.Example):
    DEFAULT_MIME_TYPE: str
    VALID_MIME_RE: Pattern[str]
    file: Any
    file_name: str
    file_size: int
    file_type: Any
    service_addr: Any
    show_progress: Any
    def _check_for_upload_service(self, disco, jid: _T1) -> Coroutine[Any, Any, Optional[_T1]]: ...
    def run_simple_example(self) -> Coroutine[Any, Any, None]: ...
    def upload(self, url, headers) -> Coroutine[Any, Any, bool]: ...

def exec_example(example) -> None: ...
