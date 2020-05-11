# (generated with --quick)

from typing import Any, Dict

JenkinsClient: Any
TriggearConfig: Any
TriggearError: Any
logging: module
yaml: module

class JenkinsesClients:
    _JenkinsesClients__jenkins_clients: Dict[str, Any]
    config: Any
    def _JenkinsesClients__setup_jenkins_client(self, url: str) -> None: ...
    def __init__(self, config) -> None: ...
    def get_jenkins(self, url: str) -> Any: ...
