# (generated with --quick)

from typing import Any, List, Type

AirflowException: Any
AirflowPlugin: Any
BaseOperator: Any
GoogleCloudBaseHook: Any
GoogleCredentials: Any
apply_defaults: Any
build: Any
errors: Any
logging: module
re: module
time: module

class GoogleMLEnginePlugin(Any):
    admin_views: List[nothing]
    executors: List[nothing]
    flask_blueprints: List[nothing]
    hooks: List[Type[MLEngineHook]]
    macros: List[nothing]
    menu_links: List[nothing]
    name: str
    operators: List[Type[MLEngineTrainingOperator]]

class MLEngineHook(Any):
    __doc__: str
    _mlengine: Any
    def __init__(self, gcp_conn_id = ..., delegate_to = ...) -> None: ...
    def _get_job(self, project_id, job_id) -> Any: ...
    def _wait_for_job_done(self, project_id, job_id, interval = ...) -> Any: ...
    def create_job(self, project_id, job, use_existing_job_fn = ...) -> Any: ...
    def get_conn(self) -> Any: ...
    def normalize_mlengine_job_id(self, job_id) -> str: ...

class MLEngineTrainingOperator(Any):
    __doc__: str
    __init__: Any
    def execute(self, context) -> None: ...
