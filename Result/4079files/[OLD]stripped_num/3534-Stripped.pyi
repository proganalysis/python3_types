# (generated with --quick)

from typing import Any, Dict

dr1: Any
dr2: Any
webdriver: Any

class Driver(metaclass=MetaClassSingleton):
    __doc__: str
    connection: Any
    def connect(self) -> Any: ...

class MetaClassSingleton(type):
    __doc__: str
    _instances: Dict[MetaClassSingleton, nothing]
    def __call__(cls: MetaClassSingleton, *args, **kwargs) -> Any: ...
