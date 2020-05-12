# (generated with --quick)

from typing import Any, Coroutine, Dict, List

AttrField: Any
HtmlField: Any
Item: Any
MotorBaseOld: Any
Spider: Any
TextField: Any
asyncio: module
middleware: Any
time: module

class NameItem(Any):
    other_name: Any
    top_name: Any

class QidianRankingSpider(Any):
    concurrency: int
    qidian_type: Dict[str, str]
    start_urls: List[str]
    def parse(self, res) -> Coroutine[Any, Any, None]: ...
    def save(self, res_dic) -> Coroutine[Any, Any, None]: ...

class RankingItem(Any):
    book_list: Any
    more: Any
    ranking_title: Any
    target_item: Any
    def clean_more(self, more) -> Coroutine[Any, Any, str]: ...
    def clean_ranking_title(self, ranking_title) -> coroutine: ...
