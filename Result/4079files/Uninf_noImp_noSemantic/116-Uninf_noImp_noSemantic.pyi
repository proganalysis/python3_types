import logging
from typing import Any

class InfoFilter(logging.Filter):
    def filter(self, rec: Any): ...

logger: Any
formatter: Any
h1: Any
h2: Any
