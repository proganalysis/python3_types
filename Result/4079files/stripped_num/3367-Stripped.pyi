# (generated with --quick)

from typing import Any, TypeVar

_T1 = TypeVar('_T1')

class Listener(MockComponentB):
    args: tuple
    builder_used_for_setup: Any
    collect_metrics_called: bool
    name: Any
    post_setup_called: bool
    simulation_end_called: bool
    time_step__cleanup_called: bool
    time_step__prepare_called: bool
    time_step_called: bool
    def on_collect_metrics(self, _) -> None: ...
    def on_post_setup(self, _) -> None: ...
    def on_simulation_end(self, _) -> None: ...
    def on_time_step(self, _) -> None: ...
    def on_time_step__cleanup(self, _) -> None: ...
    def on_time_step__prepare(self, _) -> None: ...

class MockComponentA:
    args: tuple
    builder_used_for_setup: None
    name: Any
    def __init__(self, *args, name = ...) -> None: ...

class MockComponentB:
    args: tuple
    builder_used_for_setup: Any
    name: Any
    def __init__(self, *args, name = ...) -> None: ...
    def metrics(self, _, metrics: _T1) -> _T1: ...
    def setup(self, builder) -> None: ...

class NamelessComponent:
    args: tuple
    def __init__(self, *args) -> None: ...
