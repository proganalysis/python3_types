import rescrawler
from typing import Any

__version__: str

class DICOMStandardCrawler(rescrawler.ResourceCrawler):
    def __init__(self, prog: Any, ver: Any) -> None: ...
    def get_description(self): ...
    def get_url(self): ...
    def get_re(self): ...

def main() -> None: ...
