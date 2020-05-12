# (generated with --quick)

from typing import Any

json: module
requests: module
urllib: module

class ClassProperty(property):
    __doc__: str
    def __get__(self, cls, owner) -> Any: ...

class RequestUtils(object):
    @staticmethod
    def _RequestUtils__mount_url(url, pk) -> str: ...
    @staticmethod
    def delete(url, pk) -> bool: ...
    @staticmethod
    def get(url, pk = ...) -> Any: ...
