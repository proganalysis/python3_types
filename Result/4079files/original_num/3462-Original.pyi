# (generated with --quick)

from typing import Any, List, Type

BuildState: Any
DebugReporter: Any
LocalWorkflow: Any
PhabricatorAPI: Any
RemoteWorkflow: Any
Revision: Any
SOURCE_TRY: Any
TASKCLUSTER_DATE_FORMAT: Any
TASKCLUSTER_INDEX_TTL: int
TASKCLUSTER_NAMESPACE: str
datetime: Type[datetime.datetime]
get_logger: Any
logger: Any
os: module
settings: Any
stats: Any
timedelta: Type[datetime.timedelta]

class Workflow(object):
    __doc__: str
    analyzers: Any
    index_service: Any
    phabricator: Any
    queue_service: Any
    reporters: Any
    workflows: List[nothing]
    def __init__(self, reporters, analyzers, index_service, queue_service, phabricator_api) -> None: ...
    def index(self, revision, **kwargs) -> None: ...
    def publish(self, revision, issues) -> None: ...
    def run(self, revision) -> None: ...
