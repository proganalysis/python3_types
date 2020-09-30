# (generated with --quick)

from typing import Any, Callable

webapp2: Any

class WSGIApplication(Any):
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def custom_dispatcher(router, request, response) -> Any: ...
    def route(self, *args, **kwargs) -> Callable[[Any], Any]: ...
