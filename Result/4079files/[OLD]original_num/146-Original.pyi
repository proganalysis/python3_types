# (generated with --quick)

from typing import Any

DictBase: Any
NotFoundError: Any
QueryError: Any
Record: Any
json: module
unicodedata: module

class MoeDict(Any):
    API: str
    provider: str
    title: str
    def _get_url(self, word) -> str: ...
    def query(self, word: str) -> Any: ...
    def show(self, record) -> None: ...

class MoeDictTaiwanese(Any):
    API: str
    provider: str
    title: str
    def _get_url(self, word) -> str: ...
    def query(self, word: str) -> Any: ...
    def show(self, record) -> None: ...

def clean(data, clean_cf = ...) -> Any: ...
def is_other_format(char) -> bool: ...
def remove_cf(data) -> str: ...
