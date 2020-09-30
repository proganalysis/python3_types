import aiohttp
from . import abc as ni_abc
from aiohttp import web
from typing import Awaitable, Callable

def handler(create_client: Callable[[], aiohttp.ClientSession], server: ni_abc.ServerHost, cla_records: ni_abc.CLAHost) -> Callable[[web.Request], Awaitable[web.Response]]: ...
