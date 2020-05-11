# (generated with --quick)

from typing import Any, Dict, Optional, TypeVar, Union

BotPlugin: Any
DefaultConfigMixin: Any
botcmd: Any
json: module
requests: module

AnyStr = TypeVar('AnyStr', str, bytes)

class Answer(Any, Any):
    CONFIG_TEMPLATE: Dict[str, None]
    MESSAGE_LINK: str
    SURVEY_LINK: str
    answer: Any
    @staticmethod
    def construct_link(text) -> str: ...

@overload
def quote_plus(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote_plus(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
