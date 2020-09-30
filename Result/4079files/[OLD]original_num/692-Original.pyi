# (generated with --quick)

import pathlib
from typing import Any, List, Optional

CONFIG_PATH: pathlib.Path
PATH: pathlib.Path
TEST_CONFIG_PATH: pathlib.Path
aiopg: Any
client: Any
config: Any
create_engine: Any
db: Any
engine: Any
metadata: Any
pytest: Any
sa_engine: Any
tables: Any
test_config: Any
test_engine: Any
users: Any

def get_config(argv = ...) -> Any: ...
def get_db_url(config: dict) -> str: ...
def init_app(config: Optional[List[str]] = ...) -> Any: ...
def init_sample_data(engine) -> None: ...
def setup_test_db(engine) -> None: ...
def teardown_test_db(engine) -> None: ...
