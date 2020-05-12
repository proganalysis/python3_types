# (generated with --quick)

from typing import Any, Tuple

ContentType: Any
EventIndex: Any
Page: Any
PageViewRestriction: Any
RequestFactory: Any
SimplePage: Any
Site: Any
Sitemap: Any
TestCase: Any
datetime: module
get_current_site: Any
pytz: module

class TestIndexView(Any):
    def test_index_view(self) -> None: ...

class TestSitemapGenerator(Any):
    child_page: Any
    home_page: Any
    page_with_no_last_publish_date: Any
    protected_child_page: Any
    site: Any
    unpublished_child_page: Any
    def get_request_and_django_site(self, url) -> Tuple[Any, Any]: ...
    def setUp(self) -> None: ...
    def test_get_urls_uses_specific(self) -> None: ...
    def test_get_urls_with_request_site_cache(self) -> None: ...
    def test_get_urls_without_request(self) -> None: ...
    def test_items(self) -> None: ...
    def test_lastmod_uses_last_published_date(self) -> None: ...
    def test_latest_lastmod(self) -> None: ...
    def test_latest_lastmod_missing(self) -> None: ...

class TestSitemapView(Any):
    def test_sitemap_view(self) -> None: ...
