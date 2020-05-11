# (generated with --quick)

from typing import Any

JenkinsClient: Any
TriggearConfig: Any
TriggearError: Any
logging: module
yaml: module

class JenkinsesClients:
    _JenkinsesClients__jenkins_clients: dict
    config: Any
    def _JenkinsesClients__setup_jenkins_client(self, url) -> None: ...
    def __init__(self, config) -> None: ...
    def get_jenkins(self, url) -> Any: ...
