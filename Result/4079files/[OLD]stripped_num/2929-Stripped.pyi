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
    def validate(cls, value) -> None: ...

class DecimalType(CommandType):
    __doc__: str
    @classmethod
    def validate(cls, value) -> None: ...

class IncreaseDecreaseType(StringType):
    __doc__: str
    @classmethod
    def validate(cls, value) -> None: ...

class OnOffType(StringType):
    __doc__: str
    @classmethod
    def validate(cls, value) -> None: ...

class OpenCloseType(StringType):
    __doc__: str
    @classmethod
    def validate(cls, value) -> None: ...

class PercentType(DecimalType):
    __doc__: str
    @classmethod
    def validate(cls, value) -> None: ...

class StringType(CommandType):
    __doc__: str
    @classmethod
    def validate(cls, value) -> None: ...
