# (generated with --quick)

from typing import Any, Dict, List

ALL_STATUSES: List[str]
FINISHED_STATUSES: List[str]
STATUS_VALUE: Dict[str, int]
SUITES_TO_IGNORE: List[str]
ThreadPoolExecutorResult: Any
get_logger: Any
logger: Any
os: module
taskcluster: Any
time: module

class ArtifactsHandler(object):
    parent_dir: Any
    task_ids: Any
    def __init__(self, task_ids, parent_dir = ...) -> None: ...
    def download(self, test_task) -> None: ...
    def download_all(self) -> None: ...
    def generate_path(self, platform, chunk, artifact) -> str: ...
    def get(self, platform = ..., suite = ..., chunk = ...) -> list: ...
    def get_chunks(self, platform) -> set: ...
