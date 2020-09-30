# (generated with --quick)

from typing import Any

FAKE_TIME: float
WaterButlerPath: Any
asyncio: module
bundles: Any
callback: Any
celery: Any
copy: module
core_utils: Any
dest_bundle: Any
dest_path: Any
dest_provider: Any
hashlib: module
log_to_keen: Any
mock: module
mock_time: Any
move: module
patch_backend: Any
providers: Any
pytest: Any
remote_logging: Any
src_bundle: Any
src_path: Any
src_provider: Any
sys: module
tasks: Any
test_utils: Any
time: module

class TestMoveTask:
    def test_imputes_exceptions(self, event_loop, providers, bundles, callback) -> None: ...
    def test_is_task(self) -> None: ...
    def test_move_calls_move(self, event_loop, providers, bundles) -> None: ...
    def test_return_values(self, event_loop, providers, bundles, callback, src_path, dest_path, mock_time) -> None: ...
    def test_starttime_override(self, event_loop, providers, bundles, callback, mock_time) -> None: ...
