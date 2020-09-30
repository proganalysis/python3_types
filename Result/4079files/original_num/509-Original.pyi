# (generated with --quick)

from typing import Any, Optional, Tuple

ModelBase: Any
__all__: Tuple[str]
models: Any
re: module

class Platform(Any):
    VERSION_CLEAN_NONE: str
    VERSION_CLEAN_REMOVE_AFTER_DASH: str
    VERSION_CLEAN_REMOVE_COMMIT_HASH: str
    VERSION_CLEAN_STYLES: Tuple[Tuple[str, str], Tuple[str, str], Tuple[str, str]]
    code: Any
    description: Any
    display_name: Any
    icon: Any
    install_guide: Any
    latest_version: Any
    license: Any
    name: Any
    tagline: Any
    version_clean_style: Any
    website: Any
    def __str__(self) -> str: ...
    def clean_version(self, version) -> Any: ...
    def get_method(self, version) -> Optional[str]: ...
    def save(self, *args, **kwargs) -> None: ...
