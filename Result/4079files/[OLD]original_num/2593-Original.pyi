# (generated with --quick)

from typing import Any

backoff: Any
credentials: Any
discovery: Any
os: module
shutil: module
subprocess: module
time: module
yaml: module

class DeployNewAppError(Exception):
    __doc__: str

class DeploygaeWorkflow(object):
    __doc__: str
    _app_deploy_with_retry: Any
    _appengine_service: Any
    def __init__(self, credentials) -> None: ...
    def _create_app(self, project_id: str, region: str) -> None: ...
    def deploy_gae_app(self, project_id: str, django_directory_path: str, region: str = ..., is_new: bool = ...) -> str: ...
