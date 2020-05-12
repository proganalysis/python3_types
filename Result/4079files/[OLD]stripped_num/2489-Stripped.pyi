# (generated with --quick)

from typing import Any, Union

IFID_PKT_TOUT: Any
threading: module
time: module

class InterfaceState(object):
    ACTIVE: int
    IFID_TOUT: Any
    INACTIVE: int
    REVOKED: int
    TIMED_OUT: int
    __doc__: str
    _lock: threading._RLock
    _state: int
    active_since: Union[float, int]
    last_updated: float
    def is_active(self) -> bool: ...
    def is_expired(self) -> bool: ...
    def is_inactive(self) -> bool: ...
    def is_revoked(self) -> bool: ...
    def reset(self) -> None: ...
    def revoke_if_expired(self) -> None: ...
    def update(self) -> int: ...
