# (generated with --quick)

from typing import Any

Caller: Any
CallerUpdateSummary: Any
CopyNumberCallingConfig: Any
DenoisingCallingWorkspace: Any
DenoisingModel: Any
DenoisingModelConfig: Any
DenoisingModelReader: Any
FancyAdamax: Any
HHMMClassAndCopyNumberBasicCaller: Any
HybridInferenceParameters: Any
HybridInferenceTask: Any
InitialModelParametersSupplier: Any
_logger: logging.Logger
logging: module
np: module
th: Any
types: Any

class CaseDenoisingCallingTask(Any):
    temperature: Any
    def __init__(self, denoising_config, calling_config, hybrid_inference_params, shared_workspace, initial_param_supplier, input_model_path) -> None: ...
    def disengage(self) -> None: ...

class HMMCopyNumberCaller(Any):
    __doc__: str
    copy_number_basic_caller: Any
    hybrid_inference_params: Any
    log_q_c_stc_snapshot: Any
    shared_workspace: Any
    def __init__(self, calling_config, hybrid_inference_params, shared_workspace, temperature) -> None: ...
    def call(self) -> HMMCopyNumberCallerUpdateSummary: ...
    def finalize(self) -> None: ...
    def snapshot(self) -> None: ...
    def update_auxiliary_vars(self) -> None: ...

class HMMCopyNumberCallerUpdateSummary(Any):
    copy_number_log_likelihoods_s: Any
    copy_number_update_reduced: Any
    copy_number_update_s: Any
    def __init__(self, copy_number_update_s, copy_number_log_likelihoods_s, reducer) -> None: ...
    def __repr__(self) -> str: ...
    def reduce_to_scalar(self) -> Any: ...
