# (generated with --quick)

from typing import Any, Generator, NoReturn, TypeVar

Injector: Any
_logger: Any
get_logger: Any
inject: Any
itertools: module
queue: module
threading: module

T = TypeVar('T')

class AuthGrantedEvent(Event):
    __doc__: str
    auth_event_id: Any
    event_id: int
    def __init__(self, auth_event_id) -> None: ...

class AuthRequestedEvent(Event):
    __doc__: str
    event_id: int
    request_details: Any
    def __init__(self, request_details) -> None: ...

class EndOfSubmissionsEvent(Event):
    __doc__: str
    event_id: int

class Event:
    __doc__: str
    _event_id_lock: threading.Lock
    _last_event_id: int
    event_id: int
    def __init__(self) -> None: ...
    def __str__(self) -> str: ...

class EventHandler:
    __doc__: str
    handled_event_class: None
    def __str__(self) -> str: ...
    def accept(self, event) -> bool: ...
    def handle(self, event) -> NoReturn: ...

class EventManager:
    __doc__: str
    __init__: Any
    _handlers: Any
    @staticmethod
    def _event_handle_target(handler, event) -> None: ...
    def _event_thread_target(self) -> Any: ...
    @staticmethod
    def _get_classes_in_module(mod) -> Generator[Any, Any, None]: ...
    def dispatch_event(self, event) -> None: ...
    def register_all_event_handlers(self, mod) -> None: ...
    def register_event_handler(self, event_class, handler) -> None: ...
    def register_event_handler_classes(self, *event_handler_classes) -> None: ...
    def register_event_handlers(self, *event_handlers) -> None: ...

class NewSubmissionsEvent(Event):
    __doc__: str
    event_id: int

class SubmissionFinishedEvent(Event):
    __doc__: str
    event_id: int
    submission_id: Any
    def __init__(self, submission_id) -> None: ...

class SubmissionGradeExternallyUpdatedEvent(Event):
    __doc__: str
    event_id: int
    submission_id: Any
    def __init__(self, submission_id) -> None: ...

class SubmissionStartedEvent(Event):
    __doc__: str
    event_id: int
    submission_id: Any
    def __init__(self, submission_id) -> None: ...
