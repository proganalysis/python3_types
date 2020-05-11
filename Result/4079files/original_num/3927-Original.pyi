# (generated with --quick)

from typing import Any

ConfigError: Any
SingletonModel: Any
models: Any

class SiteConfig(Any):
    Meta: type
    maintenance: Any
    def __str__(self) -> str: ...
    def check_maintenance(self, force = ...) -> None: ...
