# (generated with --quick)

from typing import Callable, Dict, Tuple, Type, Union

CodeFormatFunc = Callable[[Union[int, str]], str]
CodeFormatRgbFunc = Callable[[int, int, int], str]

CodeFormatArg: Type[Union[int, str]]
_namemap: Tuple[Tuple[str, int], ...]
_stylemap: Tuple[Tuple[int, Tuple[str, ...]], ...]
_stylenums: Tuple[str, ...]
basic_names: Tuple[str, ...]
code_nums: Dict[str, Dict[str, int]]
code_nums_reverse: Dict[str, Dict[int, str]]
codeformat: Callable[[Union[int, str]], str]
codes: Dict[str, Dict[str, str]]
codes_reverse: Dict[str, Dict[str, str]]
extbackformat: Callable[[Union[int, str]], str]
extforeformat: Callable[[Union[int, str]], str]
rgbbackformat: Callable[[int, int, int], str]
rgbforeformat: Callable[[int, int, int], str]

def _add_alias_names(d: Dict[str, Dict[str, str]]) -> None: ...
def _build_code_nums() -> Dict[str, Dict[str, int]]: ...
def _build_code_nums_reverse() -> Dict[str, Dict[int, str]]: ...
def _build_codes() -> Dict[str, Dict[str, str]]: ...
def _build_codes_reverse(codes: Dict[str, Dict[str, str]]) -> Dict[str, Dict[str, str]]: ...
