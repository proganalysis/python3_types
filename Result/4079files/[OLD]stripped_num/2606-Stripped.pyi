# (generated with --quick)

import configparser
import distutils.version
from typing import Any, Dict, Generator, Optional, Tuple, Type, TypeVar

CONFIG_FILE: str
ConfigParser: Type[configparser.ConfigParser]
LooseVersion: Type[distutils.version.LooseVersion]
glob: module
json: module
logger: logging.Logger
logging: module
os: module
re: module
sys: module

AnyStr = TypeVar('AnyStr', str, bytes)

def getDescriptionAndURL(image_info, urlbase) -> Tuple[str, Any]: ...
def getImageList() -> str: ...
def getJsonOutput(url_dict, prio = ...) -> str: ...
def getPlatformPriority(platform) -> int: ...
def parseSection(items) -> Generator[Dict[str, Any], Any, None]: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
