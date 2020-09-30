# (generated with --quick)

import __future__
from typing import Any, Dict, List, Tuple, Union

SchemaMigration: Any
absolute_import: __future__._Feature
datetime: module
db: Any
models: Any
unicode_literals: __future__._Feature

class Migration(Any):
    complete_apps: List[str]
    models: Dict[str, Dict[str, Union[Dict[str, str], Tuple[str, List[nothing], Dict[str, str]]]]]
    def backwards(self, orm) -> None: ...
    def forwards(self, orm) -> None: ...
