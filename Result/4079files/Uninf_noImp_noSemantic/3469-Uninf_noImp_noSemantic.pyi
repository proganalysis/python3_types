from scrapy_proj.helpers import *
from typing import Any

class SanatatePipelineExtraMeta:
    def process_item(self, item: Any, spider: Any): ...
