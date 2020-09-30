# (generated with --quick)

from typing import Any, Dict, List

MESSAGE_TEMPLATE: Dict[str, Any]
SERVICE_NAME: str
SEVERITIES: List[str]
SYSTEM: str
argparse: module
config: Any
json: module
random: module
requests: module
sys: module

def main() -> None: ...
def parse_args() -> argparse.Namespace: ...
def send_alert(host, severity, debug) -> None: ...
