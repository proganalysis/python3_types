# (generated with --quick)

from typing import Any, Dict, Iterable, List, Optional, TypeVar, Union

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')

class TextAttributes:
    BOLD: str
    UNDERLINE: str

class TextColors:
    BLUE: str
    CYAN: str
    GREEN: str
    GREY: str
    MAGENTA: str
    RED: str
    WHITE: str
    YELLOW: str

class TextHighlights:
    BLUE: str
    CYAN: str
    GREEN: str
    GREY: str
    MAGENTA: str
    RED: str
    WHITE: str
    YELLOW: str

def _style_text(text_chunk) -> str: ...
def colored(text: str, color: Optional[str] = ..., on_color: Optional[str] = ..., attrs: Optional[Iterable[str]] = ...) -> str: ...
def definition(title, description) -> List[Dict[str, Any]]: ...
def heading(text) -> Dict[str, Any]: ...
def styled_text(text: _T0, color: _T1, attrs: _T2 = ...) -> Dict[str, Union[_T0, _T1, _T2]]: ...
