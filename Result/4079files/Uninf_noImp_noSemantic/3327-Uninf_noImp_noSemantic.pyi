import scrapy
from typing import Any

class QuotesSpider(scrapy.Spider):
    name: str = ...
    def start_requests(self) -> None: ...
    def parse(self, response: Any) -> None: ...
