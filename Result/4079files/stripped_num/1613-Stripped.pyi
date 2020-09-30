# (generated with --quick)

import click.core
from typing import Any

Scene: Any
click: module
io: Any
landsat8_datasource_id: Any
logger: logging.Logger
logging: module
reprocess_geotiff_to_cog: click.core.Command
sentinel2_datasource_id: Any
subprocess: module
wrap_rollbar: Any

def metadata_to_postgres(scene_id) -> bool: ...
def process_id(scene_id) -> None: ...
