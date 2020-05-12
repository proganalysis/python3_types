# (generated with --quick)

from typing import Any, List, Type, Union

AirflowPlugin: Any
BaseOperator: Any
BaseSensorOperator: Any
apply_defaults: Any
datetime: Type[datetime.datetime]
log: logging.Logger
logging: module

class MyFirstOperator(Any):
    __init__: Any
    def execute(self, context) -> None: ...

class MyFirstPlugin(Any):
    name: str
    operators: List[Type[Union[MyFirstOperator, MyFirstSensor]]]

class MyFirstSensor(Any):
    __init__: Any
    def poke(self, context) -> bool: ...
