# (generated with --quick)

from typing import Any

DATA_DIRECTORY: Any
Fore: Any
os: module
shutil: module
stat: module
subprocess: module
template_zip: str
venv: module

class ExtendVenv(Any):
    _dj_version: Any
    _project_name: Any
    prod_db: Any
    def __init__(self, project_name, *args, **kwargs) -> None: ...
    def _startproject(self, context) -> None: ...
    def post_setup(self, context) -> None: ...

class SingleVenv(Any):
    __doc__: str
    dj_version: Any
    def __init__(self, dj_version, *args, **kwargs) -> None: ...
    def _requirements(self, context) -> None: ...
    def post_setup(self, context) -> None: ...

def create(project_name: str, dj_version: str, prod_db: str) -> None: ...
