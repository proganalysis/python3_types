# (generated with --quick)

from typing import Any, Coroutine

ContainerComponent: Any
Context: Any
asyncio: module
run_application: Any

class ApplicationComponent(Any):
    def start(self, ctx) -> Coroutine[Any, Any, None]: ...

class Book:
    author: Any
    isbn: Any
    name: Any
    sequel: Any
    year: Any
    def __init__(self, name, author, year, isbn, sequel = ...) -> None: ...
