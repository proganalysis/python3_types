# (generated with --quick)

from typing import Any

DjangoBaseCommand: Any
logging: module
warnings: module

class BaseCommand(Any):
    __doc__: str
    logger_name: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def execute(self, *args, **options) -> Any: ...
    @staticmethod
    def get_logger_level(verbosity) -> int: ...
