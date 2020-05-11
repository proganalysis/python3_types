# (generated with --quick)

import collections
from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar, Union

os: module
yaml: Any

_Tnamedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs = TypeVar('_Tnamedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs', bound=`namedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs`)
_Tnamedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs = TypeVar('_Tnamedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs', bound=`namedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs`)

class BuildConfig(`namedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs`):
    def check(self) -> None: ...
    def dump(self) -> None: ...
    @classmethod
    def from_kwargs(cls, workspace, **kwargs) -> Any: ...
    @classmethod
    def from_string(cls, src) -> Any: ...
    @classmethod
    def from_workspace(cls, path) -> Any: ...

class ImageConfig(`namedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs`):
    @classmethod
    def from_kwargs(cls, name, **kwargs) -> Any: ...

class `namedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs`(tuple):
    __slots__ = ["branches", "environment", "image_configs", "name", "plugin_configs", "stages", "version", "workspace"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str, str, str, str]
    branches: Any
    environment: Any
    image_configs: Any
    name: Any
    plugin_configs: Any
    stages: Any
    version: Any
    workspace: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs`], version, name, workspace, environment, branches, stages, image_configs, plugin_configs) -> `_Tnamedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs`: ...
    def _replace(self: `_Tnamedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs`, **kwds) -> `_Tnamedtuple-_BuildConfig-version-name-workspace-environment-branches-stages-image_configs-plugin_configs`: ...

class `namedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs`(tuple):
    __slots__ = ["build", "context", "environment", "from_image", "name", "plugin_configs", "run", "stage", "start", "volumes"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str, str, str, str, str, str]
    build: Any
    context: Any
    environment: Any
    from_image: Any
    name: Any
    plugin_configs: Any
    run: Any
    stage: Any
    start: Any
    volumes: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any, Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs`], name, stage, from_image, environment, volumes, context, build, run, start, plugin_configs) -> `_Tnamedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs`: ...
    def _replace(self: `_Tnamedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs`, **kwds) -> `_Tnamedtuple-_ImageConfig-name-stage-from_image-environment-volumes-context-build-run-start-plugin_configs`: ...

def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
