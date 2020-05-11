# (generated with --quick)

import collections
import functools
from typing import Any, Dict, Pattern, Type, Union
import wordinserter.operations

BaseParser: Any
Bold: Type[wordinserter.operations.Bold]
BulletList: Type[wordinserter.operations.BulletList]
CodeBlock: Type[wordinserter.operations.CodeBlock]
Footnote: Type[wordinserter.operations.Footnote]
Format: Type[wordinserter.operations.Format]
Group: Type[wordinserter.operations.Group]
Heading: Type[wordinserter.operations.Heading]
HyperLink: Type[wordinserter.operations.HyperLink]
IgnoredOperation: Type[wordinserter.operations.IgnoredOperation]
Image: Type[wordinserter.operations.Image]
Italic: Type[wordinserter.operations.Italic]
LineBreak: Type[wordinserter.operations.LineBreak]
ListElement: Type[wordinserter.operations.ListElement]
MAPPING: Dict[str, Union[type, functools.partial[nothing]]]
NumberedList: Type[wordinserter.operations.NumberedList]
Paragraph: Type[wordinserter.operations.Paragraph]
Span: Type[wordinserter.operations.Span]
Style: Type[wordinserter.operations.Style]
Table: Type[wordinserter.operations.Table]
TableBody: Type[wordinserter.operations.TableBody]
TableCell: Type[wordinserter.operations.TableCell]
TableHead: Type[wordinserter.operations.TableHead]
TableRow: Type[wordinserter.operations.TableRow]
Text: Type[wordinserter.operations.Text]
UnderLine: Type[wordinserter.operations.UnderLine]
_COLLAPSE_REGEX: Pattern[str]
bs4: Any
correct_whitespace: Any
cssutils: Any
defaultdict: Type[collections.defaultdict]
normalize_list_elements: Any
normalize_table_colspans: Any
partial: Type[functools.partial]
re: module

class HTMLParser(Any):
    def _build_format(self, element, style) -> wordinserter.operations.Format: ...
    def build_element(self, element) -> Any: ...
    def parse(self, content, stylesheets = ...) -> wordinserter.operations.Group: ...
    def recursively_add_children(self, parent, child) -> None: ...
