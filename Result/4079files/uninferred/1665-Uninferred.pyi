from typing import Any

def on_message(client: Any, userdata: Any, msg: Any) -> None: ...
def on_connect(client: Any, *args: Any) -> None: ...

iden: Any

def setupmqtt() -> None: ...
def main() -> None: ...
