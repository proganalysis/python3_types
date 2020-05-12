# (generated with --quick)

from typing import Any, Coroutine, List

AppConfig: Any
finish: Any

class TrackmaniaConfig(Any):
    app_dependencies: List[str]
    core: bool
    game_dependencies: List[str]
    name: str
    def on_start(self) -> Coroutine[Any, Any, None]: ...
