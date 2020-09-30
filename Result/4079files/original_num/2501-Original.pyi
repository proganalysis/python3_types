# (generated with --quick)

from typing import Any, Callable, List, Optional

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
    def collect_results(self, results: List[dict]) -> None: ...
    def next_to_execute(self) -> Any: ...

class LabelRunner(Any):
    _postprocess: Optional[Callable[[List[str]], List[str]]]
    loss_names: List[str]
    def __init__(self, output_series: str, decoder, postprocess: Optional[Callable[[List[str]], List[str]]] = ...) -> None: ...
    def get_executable(self, compute_losses = ..., summaries = ...) -> LabelRunExecutable: ...
