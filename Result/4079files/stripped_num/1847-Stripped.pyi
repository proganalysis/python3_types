# (generated with --quick)

from typing import Any, Dict

pprint: module

class CommandManager:
    _devices: Dict[str, Any]
    audio_driver: Any
    messaging: Any
    def __init__(self, audio_driver, messaging) -> None: ...
    def handle_command(self, msg) -> None: ...
