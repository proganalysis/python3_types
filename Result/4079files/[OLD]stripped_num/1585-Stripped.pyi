# (generated with --quick)

import collections
from typing import Any, Callable, IO, Iterable, Optional, Sized, Tuple, Type, TypeVar, Union

AddTemplateCommand: Any
CONFIG_DIR: Any
CONFIG_EXT: Any
HOME_DIR: Any
InputError: Any
ProgramData: Any
RmTemplateCommand: Any
Role: Any
RoleCommand: Any
SyncCommand: Any
TEMPLATES_DIR: Any
TemplateFile: Any
UserConfigFile: Any
add_ext: Any
builtins: module
codot: Any
copy_config: Any
fake_files: Any
os: module
pytest: Any
rm_ext: Any
subprocess: module
sys: module
textwrap: module

_TFakeFilePaths = TypeVar('_TFakeFilePaths', bound=FakeFilePaths)

class FakeFilePaths(tuple):
    __slots__ = ["config", "role", "template"]
    __dict__: collections.OrderedDict[str, Any]
    _field_defaults: collections.OrderedDict[str, Any]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str]
    config: Any
    role: Any
    template: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TFakeFilePaths], role, config, template) -> _TFakeFilePaths: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[_TFakeFilePaths], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> _TFakeFilePaths: ...
    def _replace(self: _TFakeFilePaths, **kwds) -> _TFakeFilePaths: ...

class TestAddTemplateCommand:
    patch_editor: Any
    def test_add_new_template(self, fake_files, patch_editor) -> None: ...
    def test_add_revised_template(self, fake_files, patch_editor) -> None: ...

class TestRmTemplateCommand:
    def test_nonexistent_template(self, fake_files) -> None: ...
    def test_remove_template_file(self, fake_files) -> None: ...
    def test_remove_unused_options(self, fs, fake_files) -> None: ...

class TestRoleCommand:
    test_symlink_created: Any
    def test_config_nonexistent(self, fake_files) -> None: ...
    def test_no_config_specified(self, fake_files) -> None: ...
    def test_no_role_specified(self) -> None: ...
    def test_role_nonexistent(self, fake_files) -> None: ...

class TestSyncCommand:
    test_overwrite_source_files: Any
    test_propagate_config_changes: Any
    def test_missing_identifiers(self, fs, fake_files) -> None: ...
    def test_missing_source_files(self, fs, fake_files) -> None: ...

def real_open(file: Union[_PathLike, bytes, int, str], mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., errors: Optional[str] = ..., newline: Optional[str] = ..., closefd: bool = ...) -> IO: ...
