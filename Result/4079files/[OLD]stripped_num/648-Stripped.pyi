# (generated with --quick)

from typing import Any, Tuple, TypeVar, Union

environ: Any
re: module
typing: module

_T1 = TypeVar('_T1')
_T3 = TypeVar('_T3')

def choice(title, prompt, choices, default_index: _T3 = ...) -> Tuple[Union[int, _T3], Any]: ...
def confirm(question, default: _T1 = ...) -> Union[bool, _T1]: ...
