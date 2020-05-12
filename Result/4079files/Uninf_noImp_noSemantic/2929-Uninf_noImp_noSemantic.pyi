import abc
import datetime
import typing
from typing import Any

__author__: str
__license__: str

class CommandType(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def validate(cls: Any, value: typing.Any) -> Any: ...

class StringType(CommandType):
    @classmethod
    def validate(cls: Any, value: str) -> Any: ...

class OnOffType(StringType):
    @classmethod
    def validate(cls: Any, value: str) -> Any: ...

class OpenCloseType(StringType):
    @classmethod
    def validate(cls: Any, value: str) -> Any: ...

class DecimalType(CommandType):
    @classmethod
    def validate(cls: Any, value: typing.Union[float, int]) -> Any: ...

class PercentType(DecimalType):
    @classmethod
    def validate(cls: Any, value: typing.Union[float, int]) -> Any: ...

class IncreaseDecreaseType(StringType):
    @classmethod
    def validate(cls: Any, value: str) -> Any: ...

class DateTimeType(CommandType):
    @classmethod
    def validate(cls: Any, value: datetime.datetime) -> Any: ...
