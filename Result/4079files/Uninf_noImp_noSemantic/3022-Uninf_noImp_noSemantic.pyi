from typing import Any

pickle_db: str
log: Any
swarm_master: Any
dns_updater: Any

def new_record(docker_id: Any, hostname: Any, ip: Any) -> None: ...
def delete_record(docker_id: Any) -> None: ...
def manage_event(event: Any): ...
def main() -> None: ...
