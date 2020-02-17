# (generated with --quick)

import collections
import requests.packages.urllib3.exceptions
from typing import Any, Generator, Optional, Type

APP_PATH: Any
Archive: Any
BuildConfig: Any
ComposeProject: Any
Container: Any
DockerClient: Any
Event: Any
ImageConfig: Any
OrderedDict: Type[collections.OrderedDict]
PluginManager: Any
ReadTimeoutError: Type[requests.packages.urllib3.exceptions.ReadTimeoutError]
SCRIPT_PATH: Any
Script: Any
Service: Any
VolumeSpec: Any
docker_constants: Any
os: module
struct: module
time: module

class Builder:
    args: Any
    build_num: Any
    client: Any
    commit_info: Any
    config: Any
    image_builders: Generator[Any, Any, None]
    images: collections.OrderedDict[Any, collections.OrderedDict[Any, ImageBuilder]]
    job_num: Any
    plugins: Any
    test_name: str
    test_tag: str
    def __init__(self, build_config, args = ..., build_num = ..., job_num = ..., commit_info = ...) -> None: ...
    def _stage_to_image_builders_mapping(self) -> collections.OrderedDict[Any, collections.OrderedDict[Any, ImageBuilder]]: ...

class ImageBuilder:
    archive: Any
    builder: Any
    client: Any
    config: Any
    environment: dict
    exception: Optional[Exception]
    script: Any
    volumes: Any
    def __init__(self, builder, image_config) -> None: ...
    def _run_test_container(self, service, reports) -> Any: ...
    def build(self, e) -> int: ...
    def create(self, script, labels = ...) -> Any: ...
    def ensure_from_image(self) -> None: ...
    def execute(self, modes = ...) -> None: ...
    def notify(self, event, extra = ...) -> None: ...
    def run(self, e) -> Any: ...
    def start(self, e) -> Any: ...
    def start_and_commit(self, container, cmd, e) -> int: ...

def read_container_log_for_seconds(container, secs) -> Any: ...
