# (generated with --quick)

from typing import Any, List, NoReturn

APIStrategy: Any
AbsCommand: Any
DB: Any
Decision: Any
HtmlFile: Any
Multi: Any
Request: Any
Save: Any
ScrapeMethod: Any
SeleniumStrategy: Any
SessionStrategy: Any
SourceStrategy: Any
auth: Any
ids_validator: Any
logging: module
os: module
save_wrapper: Any
settings: Any
shutil: module
source_validator: Any
sys: module
tempfile: module
unpack_archive: Any
userkey_validator: Any

class CommentsCommand(Any):
    name: str
    def execute(self, *args) -> None: ...

class DeleteCommand(Any):
    name: str
    @staticmethod
    def create_msg(arg) -> str: ...
    @staticmethod
    def delete_from_db(ids) -> None: ...
    @staticmethod
    def delete_from_wykop(ids) -> None: ...
    def execute(self, arg, *args) -> NoReturn: ...
    @staticmethod
    def get_ids() -> Any: ...

class FileSourceCommand(Any):
    name: str
    def execute(self, *args) -> None: ...

class HtmlCommand(Any):
    name: str
    def execute(self, arg, *args) -> NoReturn: ...

class IdsCommand(Any):
    name: str
    def execute(self, *args) -> None: ...

class NewCommand(Any):
    name: str
    def execute(self, *args) -> None: ...

class NsfwCommand(Any):
    name: str
    def execute(self, *args) -> None: ...

class PdkCommand(Any):
    name: str
    def execute(self, *args) -> None: ...

class SaveCommand(Any):
    name: str
    def execute(self, *args) -> NoReturn: ...

class ScrapeCommand(Any):
    name: str
    def execute(self, *args) -> None: ...

class SeleniumCommand(Any):
    name: str
    def execute(self, arg, *args) -> None: ...

class SessionCommand(Any):
    name: str
    def execute(self, *args) -> None: ...

class SkipCommand(Any):
    name: str
    def execute(self, arg, *args) -> None: ...

class UpdateCommand(Any):
    base_dir: Any
    file_name: Any
    master_zip_url: Any
    msg_err: str
    name: str
    save_file: Any
    selenium_drivers_path: Any
    def __init__(self) -> None: ...
    def choose(self) -> Any: ...
    def delete_selenium_driver_files(self) -> None: ...
    def execute(self, arg, *args) -> NoReturn: ...
    def save_and_unpack(self) -> None: ...

def copy_tree(src: str, dst: str, preserve_mode: int = ..., preserve_times: int = ..., preserve_symlinks: int = ..., update: int = ..., verbose: int = ..., dry_run: int = ...) -> List[str]: ...
