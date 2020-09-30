# (generated with --quick)

from typing import Any, Dict, Generator, List

BeautifulSoup: Any
CrawlerProcess: Any
process: Any
scrapy: Any
time: module
webdriver: Any

class ProductSpider(Any):
    allowed_domains: List[str]
    name: str
    start_urls: List[str]
    def parse(self, response) -> Generator[Dict[str, Any], Any, None]: ...
