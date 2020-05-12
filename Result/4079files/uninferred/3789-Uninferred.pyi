from typing import Any

need_clean: bool
MSG: str
DOOR_MSG: Any

def send_msg(opened: bool) -> Any: ...

PIN: int
next_state: bool
