# (generated with --quick)

from typing import Any, NoReturn, Type
import zipfile

BaseCommand: Any
CommandError: Any
ImageSet: Any
Q: Any
ZipFile: Type[zipfile.ZipFile]
fasteners: Any
os: module
settings: Any

class Command(Any):
    help: str
    def _regenerate_zip(self, imageset) -> None: ...
    def handle(self, *args, **options) -> NoReturn: ...

def sleep(secs: float) -> None: ...
