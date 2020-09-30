# (generated with --quick)

import io
from typing import Any, NoReturn, Type
import zipfile

BytesIO: Type[io.BytesIO]
CharField: Any
PolymorphicModel: Any
URLField: Any
ZipFile: Type[zipfile.ZipFile]
os: module
requests: module
secrets: module
settings: Any
sh: Any
shutil: module
string: module
tempfile: module

class Editor(Any):
    __doc__: str
    url: Any
    @staticmethod
    def create(type) -> Any: ...
    def pull(self, archive) -> NoReturn: ...
    def push(self, archive) -> NoReturn: ...

class NativeEditor(Editor):
    __doc__: str
    base_url: Any
    key: Any
    url: str
    def pull(self) -> io.BytesIO: ...
    def push(self, archive) -> None: ...
    def save(self, *args, **kwargs) -> None: ...
