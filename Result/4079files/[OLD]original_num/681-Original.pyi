# (generated with --quick)

from typing import Any, Tuple

BBox: Any
BaseCommand: Any
Color: Any
Dataset: Any
Service: Any
StretchedRenderer: Any
VARS: Tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]
Variable: Any
WGS84: str
YEARS: Tuple[str, str, str, str, str, str, str, str]
numpy: module
os: module
pyproj: Any
transaction: Any

class Command(Any):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, region_name, *args, **options) -> None: ...
