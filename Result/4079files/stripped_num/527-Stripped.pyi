# (generated with --quick)

from typing import Any, Dict, List

TelexPlugin: Any

class EmoticonsPlugin(Any):
    patterns: Dict[str, str]
    usage: List[str]
    def lod(self, msg, matches) -> bytes: ...
    def lolidk(self, msg, matches) -> bytes: ...
