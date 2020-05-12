from enum import Enum
from hvapi.common import RangedCodeEnum
from typing import Any

class Msvm_ConcreteJob_JobState(RangedCodeEnum):
    New: int = ...
    Starting: int = ...
    Running: int = ...
    Suspended: int = ...
    ShuttingDown: int = ...
    Completed: int = ...
    Terminated: int = ...
    Killed: int = ...
    Exception: int = ...
    Service: int = ...
    DMTF_Reserved: Any = ...
    Vendor_Reserved: Any = ...

class VirtualMachineStateInternal(str, Enum):
    Other: str = ...
    Running: str = ...
    Off: str = ...
    Stopping: str = ...
    Saved: str = ...
    Paused: str = ...
    Starting: str = ...
    Reset: str = ...
    Saving: str = ...
    Pausing: str = ...
    Resuming: str = ...
    FastSaved: str = ...
    FastSaving: str = ...
    ForceShutdown: str = ...
    ForceReboot: str = ...
    RunningCritical: str = ...
    OffCritical: str = ...
    StoppingCritical: str = ...
    SavedCritical: str = ...
    PausedCritical: str = ...
    StartingCritical: str = ...
    ResetCritical: str = ...
    SavingCritical: str = ...
    PausingCritical: str = ...
    ResumingCritical: str = ...
    FastSavedCritical: str = ...
    FastSavingCritical: str = ...
    def to_virtual_machine_state(self): ...

class ComputerSystem_RequestStateChange_RequestedState(RangedCodeEnum):
    Other: int = ...
    Running: int = ...
    Off: int = ...
    Stopping: int = ...
    Saved: int = ...
    Paused: int = ...
    Starting: int = ...
    Reset: int = ...
    Saving: int = ...
    Pausing: int = ...
    Resuming: int = ...
    FastSaved: int = ...
    FastSaving: int = ...
    def to_ComputerSystem_EnabledState(self): ...

class ComputerSystem_RequestStateChange_ReturnCodes(RangedCodeEnum):
    Completed_with_No_Error: int = ...
    Method_Parameters_Checked_Transition_Started: int = ...
    Access_Denied: int = ...
    Invalid_state_for_this_operation: int = ...

class ComputerSystem_EnabledState(RangedCodeEnum):
    Unknown: int = ...
    Other: int = ...
    Enabled: int = ...
    Disabled: int = ...
    ShuttingDown: int = ...
    NotApplicable: int = ...
    EnabledButOffline: int = ...
    InTest: int = ...
    Deferred: int = ...
    Quiesce: int = ...
    Starting: int = ...
    def to_virtual_machine_state(self): ...

class ShutdownComponent_OperationalStatus(RangedCodeEnum):
    OK: int = ...
    Degraded: int = ...
    NonRecoverableError: int = ...
    NoContact: int = ...
    LostCommunication: int = ...

class ShutdownComponent_ShutdownComponent_ReturnCodes(RangedCodeEnum):
    Completed_with_No_Error: int = ...
    Method_Parameters_Checked_JobStarted: int = ...
    Failed: int = ...
    Access_Denied: int = ...
    Not_Supported: int = ...
    Status_is_unknown: int = ...
    Timeout: int = ...
    Invalid_parameter: int = ...
    System_is_in_use: int = ...
    Invalid_state_for_this_operation: int = ...
    Incorrect_data_type: int = ...
    System_is_not_available: int = ...
    Out_of_memory: int = ...
    File_not_found: int = ...
    The_system_is_not_ready: int = ...
    The_machine_is_locked_and_cannot_be_shut_down_without_the_force_option: int = ...
    A_system_shutdown_is_in_progress: int = ...

class VSMS_ModifySystemSettings_ReturnCode(RangedCodeEnum):
    Completed_with_No_Error: int = ...
    Not_Supported: int = ...
    Failed: int = ...
    Timeout: int = ...
    Invalid_Parameter: int = ...
    Invalid_State: int = ...
    Incompatible_Parameters: int = ...
    Method_Parameters_Checked_Job_Started: int = ...
    Method_Reserved: Any = ...
    Vendor_Specific: Any = ...

class VSMS_ModifyResourceSettings_ReturnCode(RangedCodeEnum):
    Completed_with_No_Error: int = ...
    Not_Supported: int = ...
    Failed: int = ...
    Timeout: int = ...
    Invalid_Parameter: int = ...
    Invalid_State: int = ...
    Incompatible_Parameters: int = ...
    Method_Parameters_Checked_Job_Started: int = ...
    Method_Reserved: Any = ...
    Vendor_Specific: Any = ...

class VSMS_AddResourceSettings_ReturnCode(RangedCodeEnum):
    Completed_with_No_Error: int = ...
    Not_Supported: int = ...
    Failed: int = ...
    Timeout: int = ...
    Invalid_Parameter: int = ...
    Method_Parameters_Checked_Job_Started: int = ...
    Method_Reserved: Any = ...
    Vendor_Specific: Any = ...

class InvocationException(Exception): ...
