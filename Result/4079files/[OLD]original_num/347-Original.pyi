# (generated with --quick)

from typing import Any, Optional, Tuple

JobException: Any
ManagementObject: Any
Msvm_ConcreteJob_JobState: Any
VSMS_AddResourceSettings_ReturnCode: Any
VSMS_ModifyResourceSettings_ReturnCode: Any
VSMS_ModifySystemSettings_ReturnCode: Any
evaluate_invocation_result: Any
time: module

class JobWrapper(MOWrapper):
    MO_CLS: Tuple[str, str]
    Path: Any
    parent: Optional[MOWrapper]
    def wait(self) -> None: ...

class MOWrapper(Any):
    Path: Any
    parent: Any
    def __init__(self, mo, parent: Optional[MOWrapper] = ...) -> None: ...

class VirtualSystemManagementService(MOWrapper):
    MO_CLS: str
    Path: Any
    parent: Any
    def AddResourceSettings(self, AffectedConfiguration, *args) -> Any: ...
    def DefineSystem(self, SystemSettings, ResourceSettings = ..., ReferenceConfiguration = ...) -> Any: ...
    def ModifyResourceSettings(self, *args) -> Any: ...
    def ModifySystemSettings(self, SystemSettings) -> Any: ...
    def SetGuestNetworkAdapterConfiguration(self, ComputerSystem, *args) -> Any: ...
