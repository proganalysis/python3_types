from gradefast import events
from iochannels import Channel
from pyprovide import Injector
from typing import Any

class GradeBookEventHandler(events.EventHandler):
    injector: Any = ...
    def __init__(self, injector: Injector) -> None: ...
    def handle(self, event: events.Event) -> None: ...
    def _handle_sync(self, event: events.Event, gradebook_instance: Any) -> None: ...

class NewSubmissionsHandler(GradeBookEventHandler):
    handled_event_class: Any = ...
    def _handle_sync(self, event: events.NewSubmissionsEvent, gradebook_instance: Any) -> None: ...

class SubmissionStartedHandler(GradeBookEventHandler):
    handled_event_class: Any = ...
    def _handle_sync(self, event: events.SubmissionStartedEvent, gradebook_instance: Any) -> None: ...

class SubmissionFinishedHandler(GradeBookEventHandler):
    handled_event_class: Any = ...
    def _handle_sync(self, event: events.SubmissionFinishedEvent, gradebook_instance: Any) -> None: ...

class EndOfSubmissionsHandler(GradeBookEventHandler):
    handled_event_class: Any = ...
    def _handle_sync(self, event: events.EndOfSubmissionsEvent, gradebook_instance: Any) -> None: ...

class SubmissionGradeExternallyUpdatedHandler(GradeBookEventHandler):
    handled_event_class: Any = ...
    def _handle_sync(self, event: events.SubmissionGradeExternallyUpdatedEvent, gradebook_instance: Any) -> None: ...

class AuthGrantedEventHandler(GradeBookEventHandler):
    handled_event_class: Any = ...
    def _handle_sync(self, event: events.AuthGrantedEvent, gradebook_instance: Any) -> None: ...

class AuthRequestedEventHandler(events.EventHandler):
    handled_event_class: Any = ...
    channel: Any = ...
    event_manager: Any = ...
    def __init__(self, channel: Channel, event_manager: events.EventManager) -> None: ...
    def handle(self, event: events.AuthRequestedEvent) -> None: ...
