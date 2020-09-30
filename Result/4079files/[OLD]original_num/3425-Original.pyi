# (generated with --quick)

import __future__
from typing import Any, List, Tuple

migrations: Any
unicode_literals: __future__._Feature

class Migration(Any):
    dependencies: List[Tuple[str, str]]
    operations: list

def clean_org_data(apps, schema_editor) -> None: ...
def migrate_org_data(apps, schema_editor) -> None: ...
