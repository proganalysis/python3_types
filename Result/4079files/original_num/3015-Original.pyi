# (generated with --quick)

from typing import Any, List, Optional, Union

COLLECTOR: Union[MetricsProm, MetricsSimple]
__author__: str
__copyright__: str
common: Any
logging: module
pc: Any
threading: module
ty: module

class AbstractMetricCollector(object):
    __doc__: str
    conf: Any
    def __init__(self, conf) -> None: ...
    def put_input(self, ctx, result = ..., status: Optional[str] = ...) -> None: ...
    def put_loading_summary(self, total_duration: Optional[float] = ...) -> None: ...
    def put_output(self, output: str, process_time: float, status: str) -> None: ...
    def put_output_summary(self, inputs: int, files: int, total_duration: float) -> None: ...
    def put_total(self, total_duration: Optional[float] = ...) -> None: ...
    def write(self) -> None: ...

class MetricsProm(AbstractMetricCollector):
    __doc__: str
    _inp_by_status: Any
    _inp_loading_time: Any
    _outp_process_time: Any
    _outp_src_files: Any
    _outp_src_inp: Any
    _outp_status: Any
    _total_loading_duration: Any
    _total_output_time: Any
    _total_processing_time: Any
    conf: Any
    def put_input(self, ctx, result = ..., status: Optional[Union[property, str]] = ...) -> None: ...

class MetricsSimple(AbstractMetricCollector):
    __doc__: str
    _lock: threading.Lock
    _stats: List[str]
    conf: Any
    def put_input(self, ctx, result = ..., status: Optional[Union[property, str]] = ...) -> None: ...

def configure(conf) -> None: ...
