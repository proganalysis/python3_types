# (generated with --quick)

from typing import Any

Post: Any
Sitemap: Any

class PostSitemap(Any):
    changefreq: str
    limit: int
    priority: float
    def items(self) -> Any: ...
    def lastmod(self, obj) -> Any: ...
    def location(self, obj) -> Any: ...
