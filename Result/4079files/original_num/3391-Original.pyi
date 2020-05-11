# (generated with --quick)

from typing import Any, List, Tuple

migrations: Any
settings: Any

class Migration(Any):
    dependencies: List[Tuple[str, str]]
    operations: list

def update_site_backward(apps, schema_editor) -> None: ...
def update_site_forward(apps, schema_editor) -> None: ...
