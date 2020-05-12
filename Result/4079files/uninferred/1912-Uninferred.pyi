from typing import Any

class BuildConfig:
    @classmethod
    def from_kwargs(cls, workspace: Any, **kwargs: Any): ...
    @classmethod
    def from_workspace(cls, path: Any): ...
    @classmethod
    def from_string(cls, src: Any): ...
    def check(self) -> None: ...
    def dump(self) -> None: ...

class ImageConfig:
    @classmethod
    def from_kwargs(cls, name: Any, **kwargs: Any): ...
