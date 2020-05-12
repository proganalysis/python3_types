# (generated with --quick)

from typing import Any, Type
import wpi.port

LPR: int
LocalPort: Type[wpi.port.LocalPort]
RAW: int
TCPIPPort: Type[wpi.port.TCPIPPort]

class Driver:
    archive: Any
    inf_in_archive: Any
    inf_path: Any
    name: Any
    def __init__(self, name, archive = ..., inf_in_archive = ..., inf_path = ...) -> None: ...

class LPRPort(wpi.port.TCPIPPort):
    address: Any
    enable_snmp: Any
    is_enable_byte_count: Any
    port: Any
    protocol: int
    queue_name: Any
    snmp_comunity: Any
    snmp_dev_index: Any
    def __init__(self, address, port = ..., name = ..., enable_snmp = ..., snmp_dev_index = ..., snmp_comunity = ..., queue_name = ..., is_enable_byte_count = ...) -> None: ...

class ParameterError(Exception): ...

class Printer:
    driver: Any
    name: Any
    port: Any
    def __init__(self, port, driver, name = ...) -> None: ...

class RAWPort(wpi.port.TCPIPPort):
    address: Any
    enable_snmp: Any
    port: Any
    protocol: int
    snmp_comunity: Any
    snmp_dev_index: Any
    def __init__(self, address, port = ..., name = ..., enable_snmp = ..., snmp_dev_index = ..., snmp_comunity = ...) -> None: ...

class SMBPort(wpi.port.LocalPort):
    name: Any
    def __init__(self, name) -> None: ...

def ep(address, driver, name = ..., protocol = ..., ipport = ..., archive = ..., inf = ...) -> Printer: ...
