# (generated with --quick)

from typing import Any

kitchen_sink_app: Any
mako_app: Any
pytest: Any

class TestKitchenSinkApp:
    client: Any
    def test_api_index(self, client) -> None: ...
    def test_index(self, client) -> None: ...

class TestMakoApp:
    client: Any
    def test_html_request(self, client) -> None: ...
    def test_json_request(self, client) -> None: ...
    def test_json_request_with_query_params(self, client) -> None: ...
