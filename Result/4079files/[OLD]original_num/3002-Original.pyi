# (generated with --quick)

from typing import Any, List, Optional

BaseApplication: Any
CeleryBaseLoader: Any
__all__: List[str]
converter: Any
jinja2: module
logger: logging.Logger
logging: module
repository: Any
sbe: Any

class Application(Any):
    APP_PLUGINS: Any
    def init_extensions(self) -> None: ...
    def setup(self, config: Optional[type]) -> None: ...

class CeleryLoader(Any):
    flask_app_factory: str

def create_app(config: Optional[type] = ..., **kw) -> Application: ...
