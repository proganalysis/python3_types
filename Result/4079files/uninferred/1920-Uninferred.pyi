from typing import Any

call_id: int

class RPC:
    def __getattr__(self, name: Any): ...
