# (generated with --quick)

from typing import Any

MISSING_CLIENT_SECRETS_MESSAGE: str
Storage: Any
YOUTUBE_API_SERVICE_NAME: str
YOUTUBE_API_VERSION: str
YOUTUBE_READ_WRITE_SSL_SCOPE: str
build_from_document: Any
flow_from_clientsecrets: Any
httplib2: module
run_flow: Any
sys: module

class Auth(object):
    client_secrets_file: Any
    discoverydocument: Any
    def __init__(self, client_secrets_file, discoverydocument) -> None: ...
    def get_authenticated_service(self, args) -> Any: ...
