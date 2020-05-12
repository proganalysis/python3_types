# (generated with --quick)

from typing import Any

pytest: Any
socket: module
struct: module
test_ignore_garbage: Any
test_long_lived: Any
test_oob: Any
test_query_flood_garbage: Any
time: module
utils: module

def flood_buffer(msgcount) -> bytes: ...
def test_close(kresd_sock, query_before) -> None: ...
def test_pipelining(kresd_sock) -> None: ...
def test_query_flood_close(make_kresd_sock) -> None: ...
def test_query_flood_no_recv(make_kresd_sock) -> None: ...
def test_slow_lorris(kresd_sock, query_before) -> None: ...
