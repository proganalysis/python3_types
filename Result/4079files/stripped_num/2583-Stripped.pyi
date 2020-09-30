# (generated with --quick)

from typing import Any, Dict, List, Optional, Tuple, Union

funtoo_releases: Any

class KitHandler(UpgradeHandler): ...

class PythonKitHandler(KitHandler):
    settings: Dict[str, Dict[str, Optional[Union[str, List[str]]]]]
    @classmethod
    def available_upgrades(cls) -> List[Dict[str, Union[Dict[str, str], List[Dict[str, str]]]]]: ...
    def get_steps(self, new_branch, old_branch) -> Tuple[List[nothing], List[str]]: ...

class Release12UpgradeHandler(UpgradeHandler):
    _kits: List[str]
    @classmethod
    def available_upgrades(cls) -> List[Dict[str, Union[Dict[str, str], List[Dict[str, Any]]]]]: ...

class ReleaseHandler(UpgradeHandler): ...

class UpgradeHandler: ...
