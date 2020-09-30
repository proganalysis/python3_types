# (generated with --quick)

from typing import Any, Pattern

GenericDPL: Any
os: module
re: module

class DPL7(Any):
    __doc__: str
    addon_extension: str
    addons_path: str
    core_suspect_file_path: str
    plugins_dir: str
    regex_version_addon: Pattern[str]
    regex_version_core: Pattern[str]
    themes_dir: str
    def __init__(self, dir_path, plugins_dir, themes_dir, version = ..., version_major = ...) -> None: ...
