from mmc.mixins import BaseCommand as MonitoredCommand
from typing import Any

logger: Any

def get_monitoring_notebook_template_path(): ...
def get_monitoring_notebook_output_path(datestamp: Any, ext: str = ...): ...
def update_datestamp(notebook: Any, new_datestamp: Any) -> None: ...
def run_notebook(notebook: Any) -> None: ...
def export_notebook_to_html(notebook: Any, datestamp: Any, mark_as_latest: bool = ...) -> None: ...
def save_notebook(notebook: Any, datestamp: Any) -> None: ...

class Command(MonitoredCommand):
    help: str = ...
    def handle(self, *args: Any, **options: Any) -> None: ...
