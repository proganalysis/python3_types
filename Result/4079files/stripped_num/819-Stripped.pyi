# (generated with --quick)

from typing import Any, Dict, TypeVar, Union

pd: Any

_T3 = TypeVar('_T3')

def categorize(data, col_name = ..., new_col_name = ..., categories: _T3 = ..., max_categories = ...) -> Dict[Any, Union[Dict[int, Any], _T3]]: ...
def drop_columns_with_unique_values(data, max_unique_values = ...) -> None: ...
def dropna(data, axis, **params) -> None: ...
def dropna_columns(data, max_na_values = ...) -> None: ...
def dropna_rows(data, columns_name = ...) -> None: ...
