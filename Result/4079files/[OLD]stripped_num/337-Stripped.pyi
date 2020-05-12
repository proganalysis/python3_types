# (generated with --quick)

from typing import Any

BaseTask: Any
SQLAlchemyError: Any
StoragePool: Any

class PackageResultCollector(_ResultCollectorBase):
    __doc__: str
    def run(self, arguments) -> None: ...

class ResultCollector(_ResultCollectorBase):
    __doc__: str
    def run(self, arguments) -> None: ...

class _ResultCollectorBase(Any):
    __doc__: str
    def do_run(self, arguments, s3, postgres, results) -> None: ...
