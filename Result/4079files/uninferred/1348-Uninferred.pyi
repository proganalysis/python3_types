import venv
from typing import Any

template_zip: Any

class SingleVenv(venv.EnvBuilder):
    dj_version: Any = ...
    def __init__(self, dj_version: Any, *args: Any, **kwargs: Any) -> None: ...
    def post_setup(self, context: Any) -> None: ...
    def _requirements(self, context: Any) -> None: ...

class ExtendVenv(venv.EnvBuilder):
    _project_name: Any = ...
    _dj_version: Any = ...
    prod_db: Any = ...
    def __init__(self, project_name: Any, *args: Any, **kwargs: Any) -> None: ...
    def post_setup(self, context: Any) -> None: ...
    def _startproject(self, context: Any) -> None: ...

def create(project_name: str, dj_version: str, prod_db: str) -> Any: ...