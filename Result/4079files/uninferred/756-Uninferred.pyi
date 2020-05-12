from typing import Any

MAX_SOCKETS: int
MAX_ITERATIONS: int
RESERVED_NOFILE: int

def test_conn_flood(tmpdir: Any, sock_func_name: Any): ...
