from f8a_worker.base import BaseTask
from typing import Any

class _ResultCollectorBase(BaseTask):
    def do_run(self, arguments: Any, s3: Any, postgres: Any, results: Any) -> None: ...

class ResultCollector(_ResultCollectorBase):
    def run(self, arguments: Any): ...

class PackageResultCollector(_ResultCollectorBase):
    def run(self, arguments: Any): ...
