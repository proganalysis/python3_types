# (generated with --quick)

from typing import Any, List, Optional, Union

AVAILABLE_LANGUAGES: List[str]
LEMMATIZED: str
PUNKT: Any
PunktLanguageVars: Any
REPLACER: LemmaReplacer
STRING: str
__author__: List[str]
__license__: str
importlib: module
logger: Any
os: module
warnings: module

class LemmaReplacer(object):
    __doc__: str
    language: Any
    lemmata: Any
    def __init__(self, language) -> None: ...
    def _load_replacement_patterns(self) -> Any: ...
    def lemmatize(self, input_text, return_raw = ..., return_string = ...) -> Optional[Union[list, str]]: ...
