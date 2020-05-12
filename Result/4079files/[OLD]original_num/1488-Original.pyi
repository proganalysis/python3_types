# (generated with --quick)

from typing import Any, List

HighlightRule: Any
QColor: Any
QFont: Any
QJSValue: Any
QObject: Any
QQuickItem: Any
QRegularExpression: Any
QTextCharFormat: Any
QVariant: Any
SEARCH_FORMAT: Any
SyntaxHighlighter: Any
__author__: str
__copyright__: str
__credits__: List[str]
__license__: str
pyqtProperty: Any
pyqtSignal: Any
pyqtSlot: Any
re: module

class ExpSyntaxHighlighter(Any):
    __doc__: str
    _base_font: None
    _search_matched_lines: List[nothing]
    _syntax_highlighter: Any
    addHighlightMultiColorRule: Any
    addHighlightSingleColorRule: Any
    searchMatchedLines: Any
    searchMatchedLinesChanged: Any
    setSearchPattern: Any
    target: Any
    def __init__(self, parent = ...) -> None: ...
    def _setupFormat(self, color, fontSettings, colorIsForeground: bool = ...) -> Any: ...
