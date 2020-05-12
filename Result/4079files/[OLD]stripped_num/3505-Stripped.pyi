# (generated with --quick)

from typing import Any, List, Optional, Union

SUPPORTED_BUILD_SYSTEMS: List[BuildSystem]
abs_branding_file: str
arch_name_str: Any
argc: int
args_branding_options: Any
branding_file_path: str
bs: Optional[Union[BuildSystem, List[nothing]]]
bs_str: str
build_utils: Any
cmake_root: str
dev_null: str
os: module
packages: List[str]
platform_str: Any
re: module
request: BuildRequest
run_command: Any
saver: ProgressSaver
shutil: module
sys: module
system_info: Any
utils: Any

class BuildRequest(object):
    platform_: Any
    def __init__(self, platform, arch_name) -> None: ...
    def build(self, cmake_project_root_path, branding_options, dir_path, bs, package_types, saver) -> List[str]: ...
    def platform(self) -> Any: ...

class BuildSystem:
    cmake_generator_arg_: Any
    cmd_line_: Any
    name_: Any
    policy_: Any
    def __init__(self, name, cmd_line, cmake_generator_arg, policy) -> None: ...
    def cmake_generator_arg(self) -> Any: ...
    def cmd_line(self) -> Any: ...
    def name(self) -> Any: ...
    def policy(self) -> Any: ...

class ProgressSaver(object):
    cb_: Any
    progress_max_: Any
    progress_min_: Any
    def __init__(self, cb) -> None: ...
    def on_update_progress_message(self, progress, message) -> None: ...
    def update_progress_message_range(self, progress_min, progress_max, message) -> None: ...

def get_supported_build_system_by_name(name) -> Optional[BuildSystem]: ...
def print_message(progress, message) -> None: ...
def print_usage() -> None: ...
