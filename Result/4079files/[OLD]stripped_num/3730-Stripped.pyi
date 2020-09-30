# (generated with --quick)

import __future__
from typing import Any, List, Tuple

CrawlSpider: Any
DOMAIN: Any
Field: Any
Item: Any
LxmlLinkExtractor: Any
Rule: Any
URL: str
absolute_import: __future__._Feature
argparse: module
domainer: Any
parser: argparse.ArgumentParser
results: argparse.Namespace

class MyItem(Any):
    url: Any

class someSpider(Any):
    allowed_domains: List[str]
    name: str
    rules: Tuple[Any]
    start_urls: List[str]
    def parse_obj(self, response) -> MyItem: ...
