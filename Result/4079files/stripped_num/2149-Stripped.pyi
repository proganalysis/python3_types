# (generated with --quick)

from typing import Any

DEV_MODE: bool
GLib: Any
GObject: Any
Gio: Any
Ide: Any
gi: module
json: module
os: module

class GoCompletionProvider(Any, Any):
    def do_load(self, context) -> None: ...

class GoHoverProvider(Any):
    def do_prepare(self) -> None: ...

class GoService(Any):
    _client: Any
    _has_started: bool
    _supervisor: Any
    client: Any
    def _create_launcher(self) -> Any: ...
    def _ensure_started(self) -> None: ...
    def _ls_spawned(self, supervisor, subprocess) -> None: ...
    def _which_go_lanserver(self) -> str: ...
    @classmethod
    def bind_client(klass, provider) -> None: ...
    def do_stop(self) -> None: ...
    @classmethod
    def from_context(klass, context) -> Any: ...

class GoSymbolResolver(Any, Any):
    def do_load(self) -> None: ...
