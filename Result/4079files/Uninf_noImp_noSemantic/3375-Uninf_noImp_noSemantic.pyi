from typing import Any

SEVERITIES: Any
SYSTEM: str
SERVICE_NAME: str
MESSAGE_TEMPLATE: Any

def send_alert(host: Any, severity: Any, debug: Any) -> None: ...
def main() -> None: ...
def parse_args(): ...
