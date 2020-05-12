from ..core import Provider, Response
from typing import Any

class PopcornNotify(Provider):
    base_url: str = ...
    site_url: str = ...
    name: str = ...
    path_to_errors: Any = ...
    _required: Any = ...
    _schema: Any = ...
    def _prepare_data(self, data: dict) -> dict: ...
    def _send_notification(self, data: dict) -> Response: ...
