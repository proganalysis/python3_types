# (generated with --quick)

from typing import Any, Callable, Iterable, Type, TypeVar

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
    auth_event_id: int
    event_id: int
    def __init__(self, auth_event_id: int) -> None: ...

class AuthRequestedEvent(Event):
    __doc__: str
    event_id: int
    request_details: str
    def __init__(self, request_details: str) -> None: ...

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
    def accept(self, event: Event) -> bool: ...
    def handle(self, event: Event) -> None: ...

class EventManager:
    __doc__: str
    __init__: Any
    _handlers: Any
    @staticmethod
    def _event_handle_target(handler: EventHandler, event: Event) -> None: ...
    def _event_thread_target(self) -> None: ...
    @staticmethod
    def _get_classes_in_module(mod) -> Iterable[Type[EventHandler]]: ...
    def dispatch_event(self, event: Event) -> None: ...
    def register_all_event_handlers(self, mod) -> None: ...
    def register_event_handler(self, event_class: Type[T], handler: Callable[[T], None]) -> None: ...
    def register_event_handler_classes(self, *event_handler_classes: Type[EventHandler]) -> None: ...
    def register_event_handlers(self, *event_handlers: EventHandler) -> None: ...

class NewSubmissionsEvent(Event):
    __doc__: str
    event_id: int

class SubmissionFinishedEvent(Event):
    __doc__: str
    event_id: int
    submission_id: int
    def __init__(self, submission_id: int) -> None: ...

class SubmissionGradeExternallyUpdatedEvent(Event):
    __doc__: str
    event_id: int
    submission_id: int
    def __init__(self, submission_id: int) -> None: ...

class SubmissionStartedEvent(Event):
    __doc__: str
    event_id: int
    submission_id: int
    def __init__(self, submission_id: int) -> None: ...
