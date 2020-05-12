# (generated with --quick)

from typing import Any, Dict

backoff: Any
base64: module
container: Any
credentials: Any
kubernetes: Any
os: module
urllib: module
yaml: module

class DeployNewAppError(Exception):
    __doc__: str

class DeploygkeWorkflow(object):
    __doc__: str
    _container_client: Any
    _credentials: Any
    _try_get_ingress_url: Any
    _try_get_ready_replicas: Any
    def __init__(self, credentials) -> None: ...
    def _get_ingress_url(self, kube_config) -> str: ...
    def _wait_for_deployment_ready(self, kube_config, app_name: str) -> None: ...
    def deploy_new_app_sync(self, project_id: str, cluster_name: str, app_directory: str, app_name: str, image_name: str, secrets: Dict[str, Dict[str, str]], region: str = ..., zone: str = ...) -> str: ...
    def update_app_sync(self, project_id: str, cluster_name: str, app_directory: str, app_name: str, image_name: str, zone: str = ...) -> str: ...
