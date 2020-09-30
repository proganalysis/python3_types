# (generated with --quick)

from typing import Any, List, Optional, Pattern
import xml.etree.ElementTree

ET: module
ghostscript: Any
gslog: logging.Logger
logging: module
re: module
regex_remove_char_tags: Pattern[bytes]

def extract_text_xml(infile, pdf, pageno = ..., log = ...) -> List[Optional[xml.etree.ElementTree.Element]]: ...
def page_get_textblocks(infile, pageno, xmltext, height) -> list: ...
