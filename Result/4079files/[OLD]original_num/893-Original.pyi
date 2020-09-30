# (generated with --quick)

from typing import Any, List

BaseBackend: Any
REGEX: str
_log: logging.Logger
get_versions_by_regex: Any
logging: module

class GnomeBackend(Any):
    __doc__: str
    examples: List[str]
    name: str
    @classmethod
    def get_version(cls, project) -> Any: ...
    @classmethod
    def get_version_url(cls, project) -> str: ...
    @classmethod
    def get_versions(cls, project) -> Any: ...

def use_gnome_cache_json(project) -> Any: ...
def use_gnome_regex(project) -> Any: ...
