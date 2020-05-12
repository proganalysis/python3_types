# (generated with --quick)

from typing import Any, Generator, Tuple

escape_html: Any
formatters: Any
html: Any
io: module

class MyHTMLFormatter(Any):
    def _wrap_code(self, source) -> Generator[Tuple[Any, Any], Any, None]: ...
    def _wrap_lineanchors(self, inner) -> Generator[Tuple[Any, Any], Any, None]: ...
    def _wrap_tablelinenos(self, inner) -> Generator[Tuple[int, str], Any, None]: ...
    def wrap(self, source, outfile) -> Generator[Tuple[Any, Any], Any, None]: ...
