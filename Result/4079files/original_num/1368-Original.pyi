# (generated with --quick)

from typing import Any, Dict, List, Type

DatabaseMixin: Any
DbType: Any
auth: Any
datetime: Type[datetime.datetime]
group_only: Any
plugin: Any
twx: Any

class QuotesPlugin(Any, Any):
    __doc__: str
    add_quote: Any
    add_reply: Any
    del_quote: Any
    find_quote: Any
    get_quote: Any
    get_random_quote: Any
    patterns: Dict[str, str]
    primary_key: str
    schema: Dict[str, Any]
    usage: List[str]
    def __init__(self) -> None: ...
