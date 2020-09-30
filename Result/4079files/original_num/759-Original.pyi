# (generated with --quick)

from typing import Any, Dict

asyncio: module
datetime: module
hashlib: module
ipdb: Any
json: module
os: module
ped_parser: Any
psycopg2: Any
uuid: module

class VariantManager:
    def __init__(self) -> None: ...
    def get(self, reference_id, variant_id, analysis_id = ...) -> Dict[str, Any]: ...

def __getattr__(name) -> Any: ...
