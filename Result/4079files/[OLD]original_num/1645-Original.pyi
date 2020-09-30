# (generated with --quick)

from typing import Any, TypeVar, Union

ExecutePreprocessor: Any
HTMLExporter: Any
MonitoredCommand: Any
logger: logging.Logger
logging: module
monitoring: Any
nbformat: Any
os: module
re: module
settings: Any

_AnyPath = TypeVar('_AnyPath', str, _PathLike[str])

class Command(Any):
    help: str
    def handle(self, *args, **options) -> None: ...

def copyfile(src: Union[str, _PathLike[str]], dst: _AnyPath, *, follow_symlinks: bool = ...) -> _AnyPath: ...
def export_notebook_to_html(notebook, datestamp, mark_as_latest = ...) -> None: ...
def get_monitoring_notebook_output_path(datestamp, ext = ...) -> str: ...
def get_monitoring_notebook_template_path() -> str: ...
def run_notebook(notebook) -> None: ...
def save_notebook(notebook, datestamp) -> None: ...
def update_datestamp(notebook, new_datestamp) -> None: ...
