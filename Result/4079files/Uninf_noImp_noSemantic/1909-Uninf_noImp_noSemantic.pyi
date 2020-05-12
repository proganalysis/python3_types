from typing import Any

class TableFileSet:
    _table_file_set_classifier: Any = ...
    file_names: Any = ...
    _feature_classes: Any = ...
    _filesuffixes: Any = ...
    _feature_list_table: Any = ...
    _features: Any = ...
    _filter: Any = ...
    def __init__(self, key: Any, query_result: Any, features: Any, **kwargs: Any) -> None: ...
    def __repr__(self): ...
    def __str__(self): ...
    def detail(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    @property
    def classifier(self): ...
    @property
    def features(self): ...
    @property
    def filenames(self): ...
    @property
    def feature_classes(self): ...
    @property
    def filesuffixes(self): ...
    @property
    def study(self): ...
    @property
    def pathogen(self): ...
    @property
    def library(self): ...
    @property
    def design(self): ...
    @property
    def replicate(self): ...
    @property
    def plate(self): ...
