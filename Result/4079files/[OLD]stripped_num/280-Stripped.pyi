# (generated with --quick)

from typing import Any, List, Tuple

migrations: Any
models: Any
oauth2_provider: Any

class Migration(Any):
    dependencies: List[Tuple[str, str]]
    operations: list

def populate_columns(apps, schema_editor) -> None: ...
def populate_columns_reverse(apps, schema_editor) -> None: ...
