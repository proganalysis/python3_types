# (generated with --quick)

from typing import Any, Dict

unique: Any

class TableFileSet:
    _design: Any
    _feature_classes: Any
    _feature_list_table: Any
    _features: set
    _filesuffixes: Any
    _filter: Dict[str, Any]
    _lib: Any
    _pathogen: Any
    _plate: Any
    _replicate: Any
    _study: Any
    _table_file_set_classifier: Any
    classifier: Any
    design: Any
    feature_classes: Any
    features: Any
    file_names: Any
    filenames: Any
    filesuffixes: Any
    library: Any
    pathogen: Any
    plate: Any
    replicate: Any
    study: Any
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, key, query_result, features, **kwargs) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def detail(self) -> str: ...
