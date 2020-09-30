# (generated with --quick)

from typing import Any, Optional, Tuple

__author__: str
__author_email__: str
config: module
copy: module
default_args: dict
exp: module
glob: module
log_utils: module
logger: logging.Logger
logging: module
models: Any
os: module
pprint: module
viz_init: Any

def find_autoreload(out_path, global_out_path, name) -> Optional[str]: ...
def parse_args(models, model = ...) -> Any: ...
def setup_cortex(model = ...) -> Any: ...
def setup_experiment(args, model = ..., testmode = ...) -> Tuple[Any, Any]: ...
def update_args(kwargs, kwargs_to_update) -> None: ...
