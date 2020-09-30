# (generated with --quick)

from typing import Any, Tuple

SchemaValidationError: Any
TX_SCHEMA_COMMON: Tuple[Any, Any]
TX_SCHEMA_CREATE: Tuple[Any, Any]
TX_SCHEMA_PATH: str
TX_SCHEMA_TRANSFER: Tuple[Any, Any]
VOTE_SCHEMA: Tuple[Any, Any]
VOTE_SCHEMA_PATH: str
_: str
jsonschema: Any
logger: logging.Logger
logging: module
os: module
rapidjson: Any
rapidjson_schema: Any
yaml: module

def _load_schema(name) -> Tuple[str, Tuple[Any, Any]]: ...
def _validate_schema(schema, body) -> None: ...
def drop_schema_descriptions(node) -> None: ...
def validate_transaction_schema(tx) -> None: ...
def validate_vote_schema(vote) -> None: ...
