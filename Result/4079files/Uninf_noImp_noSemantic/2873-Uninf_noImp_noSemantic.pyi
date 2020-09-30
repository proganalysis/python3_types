from typing import Any, Callable, Dict, Tuple, Union

CodeFormatArg = Union[str, int]
CodeFormatFunc = Callable[[CodeFormatArg], str]
CodeFormatRgbFunc = Callable[[int, int, int], str]
_namemap: Tuple[Tuple[str, int], ...]
basic_names: Tuple[str, ...]
_stylemap: Tuple[Tuple[int, Tuple[str, ...]], ...]
_stylenums: Tuple[str, ...]
codeformat: CodeFormatFunc
extforeformat: CodeFormatFunc
extbackformat: CodeFormatFunc
rgbforeformat: CodeFormatRgbFunc
rgbbackformat: CodeFormatRgbFunc

def _build_code_nums() -> Dict[str, Dict[str, int]]: ...
def _build_code_nums_reverse() -> Dict[str, Dict[int, str]]: ...
def _build_codes() -> Dict[str, Dict[str, str]]: ...
def _build_codes_reverse(codes: Dict[str, Dict[str, str]]) -> Dict[str, Dict[str, str]]: ...
def _add_alias_names(d: Dict[str, Dict[str, str]]) -> None: ...

code_nums: Any
code_nums_reverse: Any
codes: Any
codes_reverse: Any
