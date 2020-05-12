# (generated with --quick)

import asyncio.events
from typing import Any, Callable, Optional, Type
import werkzeug.wrappers

ContainerComponent: Any
Context: Any
Kyoukai: Any
KyoukaiBaseComponent: Any
Request: Type[werkzeug.wrappers.Request]
Response: Type[werkzeug.wrappers.Response]
asyncio: module
component_types: Any
functools: module
greenlet: Any

class uWSGIAdapter(object):
    __doc__: str
    app: Any
    base_context: Any
    enter_kyoukai: Callable
    loop: Optional[asyncio.events.AbstractEventLoop]
    def __init__(self, app, base_context = ...) -> None: ...
    @classmethod
    def from_asphalt_config(cls, filename) -> Any: ...
    def run_application(self, environment, start_response) -> Any: ...

def uwsgi_entry_point(func) -> Callable: ...
