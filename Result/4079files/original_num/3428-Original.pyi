# (generated with --quick)

from typing import Any, List, Tuple

migrations: Any
os: module
pathlib: module
settings: Any
shutil: module

class Migration(Any):
    dependencies: List[Tuple[str, str]]
    operations: list

def populate_attachment_field(apps, _) -> None: ...
def reverse_populate_attachment_field(apps, _) -> None: ...
