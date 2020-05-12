from tornado import web
from typing import Any, Optional

def find_circular_references(garbage: Optional[Any] = ...): ...

class CollectHandler(web.RequestHandler):
    def get(self) -> None: ...

class DummyHandler(web.RequestHandler):
    def get(self) -> None: ...

class DummyAsyncHandler(web.RequestHandler):
    def get(self) -> None: ...

application: Any

def main() -> None: ...
