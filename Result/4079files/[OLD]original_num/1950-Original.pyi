# (generated with --quick)

import enum
from typing import Any, Tuple, Type

Enum: Type[enum.Enum]
RangedCodeEnum: Any
VirtualMachineState: Any

class ComputerSystem_EnabledState(Any):
    Deferred: int
    Disabled: int
    Enabled: int
    EnabledButOffline: int
    InTest: int
    NotApplicable: int
    Other: int
    Quiesce: int
    ShuttingDown: int
    Starting: int
    Unknown: int
    __doc__: str
    def to_virtual_machine_state(self) -> Any: ...

class ComputerSystem_RequestStateChange_RequestedState(Any):
    FastSaved: int
    FastSaving: int
    Off: int
    Other: int
    Paused: int
    Pausing: int
    Reset: int
    Resuming: int
    Running: int
    Saved: int
    Saving: int
    Starting: int
    Stopping: int
    __doc__: str
    def to_ComputerSystem_EnabledState(self) -> int: ...

class ComputerSystem_RequestStateChange_ReturnCodes(Any):
    Access_Denied: int
    Completed_with_No_Error: int
    Invalid_state_for_this_operation: int
    Method_Parameters_Checked_Transition_Started: int

class InvocationException(Exception): ...

class Msvm_ConcreteJob_JobState(Any):
    Completed: int
    DMTF_Reserved: Tuple[int, int]
    Exception: int
    Killed: int
    New: int
    Running: int
    Service: int
    ShuttingDown: int
    Starting: int
    Suspended: int
    Terminated: int
    Vendor_Reserved: Tuple[int, int]

class ShutdownComponent_OperationalStatus(Any):
    Degraded: int
    LostCommunication: int
    NoContact: int
    NonRecoverableError: int
    OK: int
    __doc__: str

class ShutdownComponent_ShutdownComponent_ReturnCodes(Any):
    A_system_shutdown_is_in_progress: int
    Access_Denied: int
    Completed_with_No_Error: int
    Failed: int
    File_not_found: int
    Incorrect_data_type: int
    Invalid_parameter: int
    Invalid_state_for_this_operation: int
    Method_Parameters_Checked_JobStarted: int
    Not_Supported: int
    Out_of_memory: int
    Status_is_unknown: int
    System_is_in_use: int
    System_is_not_available: int
    The_machine_is_locked_and_cannot_be_shut_down_without_the_force_option: int
    The_system_is_not_ready: int
    Timeout: int

class VSMS_AddResourceSettings_ReturnCode(Any):
    Completed_with_No_Error: int
    Failed: int
    Invalid_Parameter: int
    Method_Parameters_Checked_Job_Started: int
    Method_Reserved: Tuple[int, int]
    Not_Supported: int
    Timeout: int
    Vendor_Specific: Tuple[int, int]
    __doc__: str

class VSMS_ModifyResourceSettings_ReturnCode(Any):
    Completed_with_No_Error: int
    Failed: int
    Incompatible_Parameters: int
    Invalid_Parameter: int
    Invalid_State: int
    Method_Parameters_Checked_Job_Started: int
    Method_Reserved: Tuple[int, int]
    Not_Supported: int
    Timeout: int
    Vendor_Specific: Tuple[int, int]
    __doc__: str

class VSMS_ModifySystemSettings_ReturnCode(Any):
    Completed_with_No_Error: int
    Failed: int
    Incompatible_Parameters: int
    Invalid_Parameter: int
    Invalid_State: int
    Method_Parameters_Checked_Job_Started: int
    Method_Reserved: Tuple[int, int]
    Not_Supported: int
    Timeout: int
    Vendor_Specific: Tuple[int, int]
    __doc__: str

class VirtualMachineStateInternal(str, enum.Enum):
    FastSaved: str
    FastSavedCritical: str
    FastSaving: str
    FastSavingCritical: str
    ForceReboot: str
    ForceShutdown: str
    Off: str
    OffCritical: str
    Other: str
    Paused: str
    PausedCritical: str
    Pausing: str
    PausingCritical: str
    Reset: str
    ResetCritical: str
    Resuming: str
    ResumingCritical: str
    Running: str
    RunningCritical: str
    Saved: str
    SavedCritical: str
    Saving: str
    SavingCritical: str
    Starting: str
    StartingCritical: str
    Stopping: str
    StoppingCritical: str
    def to_virtual_machine_state(self) -> Any: ...
