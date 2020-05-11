# (generated with --quick)

import concurrent.futures._base
import concurrent.futures.thread
from typing import Any, AsyncGenerator, Optional, Tuple, Type
import urllib.parse

Executor: Type[concurrent.futures._base.Executor]
ThreadPoolExecutor: Type[concurrent.futures.thread.ThreadPoolExecutor]
_SSL_CONTEXT: ssl.SSLContext
aiohttp: Any
argparse: module
asyncio: module
certifi: module
ipaddress: module
iso3166: Any
json: module
logging: module
oc: Any
os: module
parser: argparse.ArgumentParser
ssl: module
sys: module

def aenumerate(inner) -> AsyncGenerator[Tuple[int, Any], Any]: ...
def atop_n(inner, n) -> asyncgenerator: ...
def main(args) -> None: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
