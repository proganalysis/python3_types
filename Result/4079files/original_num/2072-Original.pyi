# (generated with --quick)

from typing import Any, List

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

class AuthRequestedEventHandler(Any):
    __init__: Any
    handled_event_class: Any
    def handle(self, event) -> None: ...

class EndOfSubmissionsHandler(GradeBookEventHandler):
    handled_event_class: Any

class GradeBookEventHandler(Any):
    __doc__: str
    __init__: Any
    def _handle_sync(self, event, gradebook_instance) -> None: ...
    def handle(self, event) -> None: ...

class NewSubmissionsHandler(GradeBookEventHandler):
    handled_event_class: Any

class SubmissionFinishedHandler(GradeBookEventHandler):
    handled_event_class: Any

class SubmissionGradeExternallyUpdatedHandler(GradeBookEventHandler):
    handled_event_class: Any

class SubmissionStartedHandler(GradeBookEventHandler):
    handled_event_class: Any
