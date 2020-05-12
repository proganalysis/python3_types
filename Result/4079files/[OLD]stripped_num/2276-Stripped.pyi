# (generated with --quick)

from typing import Any, Optional, Type, TypeVar, Union
import xml.etree.ElementTree

Element: Type[xml.etree.ElementTree.Element]
ElementTree: Type[xml.etree.ElementTree.ElementTree]
codecs: module
config: Any
doc: xml.etree.ElementTree.ElementTree
dst: str
f: codecs.StreamReaderWriter
hmlDoc: str
hmlEquation2latex: Any
json: module
os: module
script: str
sys: module

_T0 = TypeVar('_T0')

def convertEquation(doc: _T0) -> _T0: ...
def extract2HtmlStr(doc) -> Any: ...
def fromstring(text: Union[bytes, str], parser: Optional[xml.etree.ElementTree.XMLParser] = ...) -> xml.etree.ElementTree.Element: ...
def parseHml(fileName) -> xml.etree.ElementTree.ElementTree: ...
