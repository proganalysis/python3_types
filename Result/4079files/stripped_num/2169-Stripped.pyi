# (generated with --quick)

from typing import Any

docker: Any
logger: logging.Logger
logging: module

class InvalidImage(ValidationError):
    __doc__: str

class InvalidNetwork(ValidationError):
    __doc__: str

class ValidationError(Exception):
    __doc__: str

def is_valid_image(docker_client, image) -> bool: ...
def is_valid_network(docker_client, network) -> bool: ...
