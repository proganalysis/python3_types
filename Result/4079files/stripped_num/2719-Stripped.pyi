# (generated with --quick)

from typing import Any, Optional

OPTIONS_FILE_NAME: str
arg_check: Any
argparse: module
asyncio: module
cmdline: Any
debug: Any
exceptions: Any
log: Any
master: Any
options: Any
optmanager: Any
os: module
proxy: Any
signal: module
sys: module
typing: module

def assert_utf8_env() -> None: ...
def mitmdump(args = ...) -> Optional[int]: ...
def mitmproxy(args = ...) -> Optional[int]: ...
def mitmweb(args = ...) -> None: ...
def process_options(parser, opts, args) -> Any: ...
def run(master_cls, make_parser, arguments, extra = ...) -> Any: ...
