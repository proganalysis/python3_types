# (generated with --quick)

import event
from typing import Any, Type, TypeVar
import unittest.case

EventHook: Type[event.EventHook]
unittest: module

_TProgressSpan = TypeVar('_TProgressSpan', bound=ProgressSpan)

class CompositeProgress:
    spans: Any
    target: Any
    def __init__(self, spans, target) -> None: ...
    def set(self, current, total) -> None: ...
    def update(self) -> None: ...

class CompositeProgressTest(unittest.case.TestCase):
    def test_composite_progress(self) -> None: ...

class ProgressSpan:
    current: Any
    max: Any
    min: Any
    name: Any
    on_change: event.EventHook
    def __iadd__(self: _TProgressSpan, other) -> _TProgressSpan: ...
    def __init__(self, max = ..., min = ..., name = ...) -> None: ...
    def update(self, current) -> None: ...

class ProgressSpanTest(unittest.case.TestCase):
    updated: Any
    def check_updated(self, span) -> None: ...
    def test_progress_update(self) -> None: ...
    def update(self, progress) -> None: ...
