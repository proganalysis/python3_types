# (generated with --quick)

from typing import Any, Optional, Type, Union
import xml.etree.ElementTree

Element: Type[xml.etree.ElementTree.Element]
ElementTree: Type[xml.etree.ElementTree.ElementTree]
codecs: module
config: Any
doc: str
dst: str
f: codecs.StreamReaderWriter
hmlDoc: str
hmlEquation2latex: Any
json: module
os: module
script: str
sys: module

def convertEquation(doc: xml.etree.ElementTree.ElementTree) -> str: ...
def extract2HtmlStr(doc: xml.etree.ElementTree.ElementTree) -> str: ...
def fromstring(text: Union[bytes, str], parser: Optional[xml.etree.ElementTree.XMLParser] = ...) -> xml.etree.ElementTree.Element: ...
def parseHml(fileName: str) -> xml.etree.ElementTree.ElementTree: ...
