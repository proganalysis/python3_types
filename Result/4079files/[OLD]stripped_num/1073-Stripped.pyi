# (generated with --quick)

from typing import Any

__author__: str

class Contact:
    administrative: Any
    billing: Any
    registrant: Any
    technical: Any
    def __init__(self, data) -> None: ...

class DomainInfo:
    auto_renew: Any
    contacts: Contact
    created: Any
    expires: Any
    locked: Any
    name_servers: list
    private: Any
    status: Any
    traffic_type: Any
    def __init__(self, data) -> None: ...

class NameServers:
    @staticmethod
    def process(data) -> list: ...
