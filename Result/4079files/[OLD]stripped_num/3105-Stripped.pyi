# (generated with --quick)

import pkg_resources
from typing import Any, Optional, Type, Union

APP_CFG_DIR: Any
APP_ROOT_DIR: Optional[str]
DistributionNotFound: Type[pkg_resources.DistributionNotFound]
HOME_DIR: Optional[str]
TIMESTAMP_FILE_NAME: str
TIMESTAMP_FORMAT: str
USER_CFG_FILE: Optional[str]
VERSION: Optional[str]
VersionConflict: Type[pkg_resources.VersionConflict]
os: module

def _get_version() -> str: ...
def eprint(*objects, sep = ..., end = ..., file = ..., flush = ...) -> None: ...
def get_distribution(dist: Union[str, pkg_resources.Distribution, pkg_resources.Requirement]) -> pkg_resources.Distribution: ...
def init_default_constants() -> None: ...
def set_cfg_dir(custom_dir) -> None: ...
