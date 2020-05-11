# (generated with --quick)

from typing import Any, Dict, List, Tuple

BaseRunner: Any
END_TOKEN_INDEX: Any
Executable: Any
ExecutionResult: Any
NextExecute: Any
np: module

class LabelRunExecutable(Any):
    _fetches: Any
    _postprocess: Any
    _vocabulary: Any
    all_coders: Any
    decoded_labels: List[nothing]
    result: Any
    def __init__(self, all_coders, fetches, vocabulary, postprocess) -> None: ...
    def collect_results(self, results) -> None: ...
    def next_to_execute(self) -> Tuple[Any, Any, Dict[nothing, nothing]]: ...

class LabelRunner(Any):
    _postprocess: Any
    loss_names: List[str]
    def __init__(self, output_series, decoder, postprocess = ...) -> None: ...
    def get_executable(self, compute_losses = ..., summaries = ...) -> LabelRunExecutable: ...
