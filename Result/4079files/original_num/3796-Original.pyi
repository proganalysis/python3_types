# (generated with --quick)

import entity
import logging
import typing
from typing import Any, Generator, Type

Counter: Type[typing.Counter]
Entity: Type[entity.Entity]
Logger: Type[logging.Logger]
config: Any
pyshark: Any
time: module

class Flow:
    client: entity.Entity
    end_time: float
    logger: logging.Logger
    packets: list
    protocols: typing.Counter
    server: entity.Entity
    start_time: float
    def __init__(self, pkt) -> None: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
    def count_protocol(self, pkt) -> None: ...
    def ingest(self, pkt) -> None: ...

def check_if_packet_is_upstream(pkt) -> Any: ...
