# (generated with --quick)

import jinja2.environment
import jinja2.loaders
from typing import Any, Optional, Type
import xml.etree.ElementTree

Environment: Type[jinja2.environment.Environment]
FileSystemLoader: Type[jinja2.loaders.FileSystemLoader]
HtmlFormatter: Any
LOGGER: logging.Logger
QMessageBox: Any
QUrl: Any
QUrlQuery: Any
Qgis: Any
QgsSettings: Any
XmlLexer: Any
codecs: module
etree: module
highlight: Any
loadUiType: Any
logging: module
os: module
parseString: Any
webbrowser: module

class StaticContext(object):
    __doc__: str
    ppath: str

def clean_ows_url(url) -> Any: ...
def get_connections_from_file(parent, filename) -> Optional[xml.etree.ElementTree.Element]: ...
def get_help_url() -> str: ...
def get_ui_class(ui_file) -> Any: ...
def gettext(message: str) -> str: ...
def highlight_xml(context, xml) -> str: ...
def ngettext(singular: str, plural: str, n: int) -> str: ...
def normalize_text(text) -> Any: ...
def open_url(url) -> None: ...
def prettify_xml(xml) -> Any: ...
def render_template(language, context, data, template) -> str: ...
def serialize_string(input_string) -> str: ...
