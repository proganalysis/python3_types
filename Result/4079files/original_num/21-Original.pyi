# (generated with --quick)

from typing import Any, NoReturn

Logger: Any
Plugin: Any
PluginStore: Any
State: Any
ast: module
flush_stdout: Any
multi_lines_output_handler: Any
platform: module
queue: module
subprocess: module

class _ListenerInterface(object):
    __doc__: str
    _queue_tts: queue.Queue
    _state: Any
    _store: Any
    def __init__(self, state, store, tts: queue.Queue) -> None: ...
    def _process_result(self, plugin_name: str, process: subprocess.Popen) -> None: ...
    def listen(self) -> NoReturn: ...
    def stop(self) -> None: ...
