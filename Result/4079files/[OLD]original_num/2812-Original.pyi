# (generated with --quick)

from typing import Any

BootstrapTable: Any
BtnColumn: Any
Column: Any
LinkColumn: Any
button_toolbar: Any
current_user: Any

class PortTable(Any):
    delete_link: Any
    edit_link: Any
    patchport_name: Any
    room: Any
    switch_id: Any
    switchport_name: Any
    toolbar: Any
    def __init__(self, *a, switch_id = ..., **kw) -> None: ...

class SubnetTable(Any):
    address: Any
    description: Any
    free_ips_formatted: Any
    gateway: Any
    id: Any
    reserved: Any

class SwitchTable(Any):
    delete_link: Any
    edit_link: Any
    id: Any
    ip: Any
    name: Any
    toolbar: Any

class VlanTable(Any):
    id: Any
    name: Any
    vid: Any

def no_inf_change() -> bool: ...
def url_for(endpoint, **values) -> Any: ...
