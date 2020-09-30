# (generated with --quick)

from typing import Optional

dns_updater: dnsupdate.DDNSUpdater
dnsupdate: module
log: logging.Logger
logging: module
os: module
pickle: module
pickle_db: str
swarm: module
swarm_master: swarm.SwarmClient
time: module

def delete_record(docker_id) -> None: ...
def main() -> None: ...
def manage_event(event) -> Optional[bool]: ...
def new_record(docker_id, hostname, ip) -> None: ...
