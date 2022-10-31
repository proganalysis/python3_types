from typing import Any

class TestKnoxvilleMeetingScraper:
    session: Any = ...
    page_str: str = ...
    def test_get_docs_from_page(self) -> None: ...
    def test_full_scraper(self) -> None: ...
    @classmethod
    def setup_class(cls) -> None: ...
    @classmethod
    def teardown_class(cls) -> None: ...
    def setup_method(self, test_method: Any) -> None: ...
    def teardown_method(self, test_method: Any) -> None: ...