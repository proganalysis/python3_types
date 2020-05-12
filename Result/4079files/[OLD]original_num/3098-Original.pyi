# (generated with --quick)

from typing import Any, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

Active_Emu_Profiler: Any
FunctionExperiment: Any
LOG: logging.Logger
Passive_Emu_Profiler: Any
ServiceExperiment: Any
argparse: module
coloredlogs: Any
logging: module
os: module
read_yaml: Any
tempfile: module
time: module

class ProfileManager(object):
    __doc__: str
    args: Any
    function_experiments: Any
    generated_services: List[nothing]
    output_dir: Any
    ped: Any
    service_experiments: Any
    start_time: float
    work_dir: Any
    def __init__(self, args) -> None: ...
    def _active_execution(self) -> None: ...
    @staticmethod
    def _generate_experiment_specifications(input_ped) -> Tuple[list, list]: ...
    @staticmethod
    def _load_ped_file(ped_path) -> Any: ...
    def _passive_execution(self) -> None: ...
    @staticmethod
    def _validate_ped_file(input_ped) -> None: ...
    def run(self) -> None: ...

def colored(text: str, color: Optional[str] = ..., on_color: Optional[str] = ..., attrs: Optional[Iterable[str]] = ...) -> str: ...
def main() -> None: ...
def parse_args(manual_args = ...) -> argparse.Namespace: ...
def tabulate(tabular_data: Union[Iterable[Iterable], Mapping[str, Iterable]], headers: Union[str, Sequence[str]] = ..., tablefmt: Union[str, tabulate.TableFormat] = ..., floatfmt: Union[str, Iterable[str]] = ..., numalign: Optional[str] = ..., stralign: Optional[str] = ..., missingval: Union[str, Iterable[str]] = ..., showindex: Union[bool, Iterable] = ..., disable_numparse: Union[bool, Iterable[int]] = ..., colalign: Optional[Iterable[Optional[str]]] = ...) -> str: ...
