from typing import Any

def pypi_action(action: Any): ...
def add_pypi_action_route(config: Any, name: Any, action: Any, **kwargs: Any) -> None: ...
def add_pypi_action_redirect(config: Any, action: Any, target: Any, **kwargs: Any) -> None: ...
def includeme(config: Any) -> None: ...