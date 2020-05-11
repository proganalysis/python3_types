# (generated with --quick)

from typing import Any

__author__: str
__license__: str
abc: module
datetime: module
typing: module

class CommandType(metaclass=abc.ABCMeta):
    __doc__: str
    @classmethod
    @abstractmethod
    def validate(cls, value) -> Any: ...

class DateTimeType(CommandType):
    __doc__: str
    @classmethod
    def validate(cls, value: datetime.datetime) -> None: ...

class DecimalType(CommandType):
    __doc__: str
    @classmethod
    def validate(cls, value: float) -> None: ...

class IncreaseDecreaseType(StringType):
    __doc__: str
    @classmethod
    def validate(cls, value: str) -> None: ...

class OnOffType(StringType):
    __doc__: str
    @classmethod
    def validate(cls, value: str) -> None: ...

class OpenCloseType(StringType):
    __doc__: str
    @classmethod
    def validate(cls, value: str) -> None: ...

class PercentType(DecimalType):
    __doc__: str
    @classmethod
    def validate(cls, value: float) -> None: ...

class StringType(CommandType):
    __doc__: str
    @classmethod
    def validate(cls, value: str) -> None: ...
