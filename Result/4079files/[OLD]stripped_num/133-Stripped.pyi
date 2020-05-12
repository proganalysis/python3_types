# (generated with --quick)

from typing import Any, Union

BaseConfigLoader: Any

class SlaveConfigLoader(Any):
    CONFIG_FILE_SECTION: str
    def configure_defaults(self, conf) -> None: ...
    def configure_postload(self, conf) -> None: ...

@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
