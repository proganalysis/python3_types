# (generated with --quick)

import __future__
from typing import Any, Generator, List, TypeVar, Union

GITHUB_BASEURL: str
__apk_version__: Any
__atx_agent_version__: Any
_commands: List[dict]
absolute_import: __future__._Feature
adbutils: Any
appdir: str
argparse: module
hashlib: module
humanize: Any
json: module
logger: Any
logging: module
os: module
print_function: __future__._Feature
progress: Any
re: module
requests: module
retry: Any
shutil: module
tarfile: module
u2: Any

_T1 = TypeVar('_T1')

class DownloadBar(Any):
    current_size: Any
    message: str
    suffix: str
    total_size: Any

class Initer:
    _device: Any
    abi: Any
    abis: Any
    apk_urls: Generator[str, Any, None]
    arch: Any
    atx_agent_url: str
    check_atx_agent_version: Any
    minicap_urls: Generator[str, Any, None]
    minitouch_url: str
    pre: Any
    sdk: Any
    server_addr: None
    def __init__(self, device) -> None: ...
    def install(self, server_addr = ...) -> None: ...
    def is_apk_outdate(self) -> bool: ...
    def push_url(self, url, dest: _T1 = ..., mode = ..., tgz = ..., extract_name = ...) -> Union[str, _T1]: ...
    def shell(self, *args) -> Any: ...

def cache_download(url, filename = ..., timeout = ...) -> str: ...
def cmd_console(args) -> None: ...
def cmd_current(args) -> None: ...
def cmd_healthcheck(args) -> None: ...
def cmd_identify(args) -> None: ...
def cmd_init(args) -> None: ...
def cmd_install(args) -> None: ...
def cmd_screenshot(args) -> None: ...
def cmd_start(args) -> None: ...
def cmd_stop(args) -> None: ...
def cmd_uninstall(args) -> None: ...
def main() -> None: ...
def mirror_download(url, filename) -> str: ...
