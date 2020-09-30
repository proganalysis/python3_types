from typing import Any, Optional

logger: Any
host: Any
database: Any
influxdb_client: Any

def log_to_influxdb(self, measurement: Any, fields: Any, tags: Optional[Any] = ...) -> None: ...
def log_error(_: Any, error_message: Any, module_: Any, type_: Any) -> None: ...
