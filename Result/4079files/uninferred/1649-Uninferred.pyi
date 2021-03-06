from django.contrib.sitemaps import Sitemap
from typing import Any

class PostSitemap(Sitemap):
    changefreq: str = ...
    priority: float = ...
    limit: int = ...
    def items(self): ...
    def location(self, obj: Any): ...
    def lastmod(self, obj: Any): ...
