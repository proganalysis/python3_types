# (generated with --quick)

from typing import Any, NoReturn

CustomLogger: Any
PackageCategories: Any
Plugin: Any
PluginCollection: Any
logger: Any
logging: module
results_store: Any

class BaseBuildLogHook(Any):
    CATEGORIES: Any
    __doc__: str
    @classmethod
    def format(cls, data) -> NoReturn: ...
    @classmethod
    def merge_two_results(cls, old, new) -> NoReturn: ...
    @classmethod
    def run(cls, spec_file, rebase_spec_file, results_dir, **kwargs) -> NoReturn: ...

class BuildLogHookCollection(Any):
    def run(self, spec_file, rebase_spec_file, non_interactive, force_build_log_hooks, **kwargs) -> bool: ...
