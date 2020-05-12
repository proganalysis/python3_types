from typing import Any

kernel_src: str
dev: Any
context: Any
queue: Any
prog: Any
v: Any
v_buff: Any
user_event: Any

def read_complete(status: Any, data: Any) -> None: ...

global_size: Any
local_size: Any
kernel_event: Any
read_event: Any
