# (generated with --quick)

from typing import Any

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
    def _get_ingress_url(self, kube_config) -> Any: ...
    def _wait_for_deployment_ready(self, kube_config, app_name) -> None: ...
    def deploy_new_app_sync(self, project_id, cluster_name, app_directory, app_name, image_name, secrets, region = ..., zone = ...) -> Any: ...
    def update_app_sync(self, project_id, cluster_name, app_directory, app_name, image_name, zone = ...) -> Any: ...
