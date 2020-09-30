# (generated with --quick)

import functools
from typing import Any, Type

Crumb: Any
ParameterGrid: Any
append_dict_values: Any
crumb_copy: Any
crumb_link: Any
difference: Any
groupby_pattern: Any
intersection: Any
mktree: Any
os: module
partial: Type[functools.partial]
pytest: Any
rm_dups: Any
tempfile: module
test_crumb_copy: functools.partial[nothing]
test_crumb_copy_make_link_dirs: functools.partial[nothing]
valuesmap_to_dict: Any

def _test_crumb_copy(make_links = ...) -> None: ...
def test_difference() -> None: ...
def test_group_pattern() -> None: ...
def test_intersection() -> None: ...
def test_valuesmap_to_dict(tmp_tree_crumb, brain_data_crumb_args) -> None: ...
def test_valuesmap_to_dict_raises(tmp_tree_crumb) -> None: ...
