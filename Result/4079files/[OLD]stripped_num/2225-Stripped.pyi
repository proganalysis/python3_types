# (generated with --quick)

import __future__
from typing import Any, List, Tuple

migrations: Any
models: Any
unicode_literals: __future__._Feature

class Migration(Any):
    dependencies: List[Tuple[str, str]]
    operations: list

def fix_negative_integers(apps, schema_editor) -> None: ...
