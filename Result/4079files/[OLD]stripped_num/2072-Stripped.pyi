# (generated with --quick)

from typing import Any, List, NoReturn

Channel: Any
DEFAULT_BAD_CHOICE_MSG: Any
Injector: Any
Msg: Any
__all__: List[str]
_logger: Any
events: Any
get_logger: Any
inject: Any

class AuthGrantedEventHandler(GradeBookEventHandler):
    handled_event_class: Any
    def _handle_sync(self, event, gradebook_instance) -> None: ...

class AuthRequestedEventHandler(Any):
    __init__: Any
    handled_event_class: Any
    def handle(self, event) -> None: ...

class EndOfSubmissionsHandler(GradeBookEventHandler):
    handled_event_class: Any
    def _handle_sync(self, event, gradebook_instance) -> None: ...

class GradeBookEventHandler(Any):
    __doc__: str
    __init__: Any
    def _handle_sync(self, event, gradebook_instance) -> NoReturn: ...
    def handle(self, event) -> NoReturn: ...

class NewSubmissionsHandler(GradeBookEventHandler):
    handled_event_class: Any
    def _handle_sync(self, event, gradebook_instance) -> None: ...

class SubmissionFinishedHandler(GradeBookEventHandler):
    handled_event_class: Any
    def _handle_sync(self, event, gradebook_instance) -> None: ...

class SubmissionGradeExternallyUpdatedHandler(GradeBookEventHandler):
    handled_event_class: Any
    def _handle_sync(self, event, gradebook_instance) -> None: ...

class SubmissionStartedHandler(GradeBookEventHandler):
    handled_event_class: Any
    def _handle_sync(self, event, gradebook_instance) -> None: ...
