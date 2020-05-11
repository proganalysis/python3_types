# (generated with --quick)

import logging.handlers
import pathlib
from typing import Any, Optional, Type

APP_NAME: Any
APP_VERSION: Any
COMPANY_NAME: Any
Path: Type[pathlib.Path]
ROOT_PATH: str
RotatingFileHandler: Type[logging.handlers.RotatingFileHandler]
WRITE_PATH: str
_log_path: str
_program_files: Optional[str]
formatter: logging.Formatter
handler: logging.handlers.RotatingFileHandler
logger: logging.Logger
logging: module
os: module
sys: module

def _create_write_path() -> None: ...
def get_root_path(*args) -> str: ...
def get_write_path(*args) -> str: ...
