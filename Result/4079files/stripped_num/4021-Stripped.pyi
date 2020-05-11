# (generated with --quick)

from typing import Any

BaseVersioneer: Any
CustomLogger: Any
DownloadHelper: Any
PackageCategories: Any
PackageCategory: Any
logger: Any
logging: module

class CPAN(Any):
    API_URL: str
    BASE_URL: str
    CATEGORIES: list
    @classmethod
    def _get_version(cls, package_name) -> Any: ...
    @classmethod
    def run(cls, package_name) -> Any: ...
