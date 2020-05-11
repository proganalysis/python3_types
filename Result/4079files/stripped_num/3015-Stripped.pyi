# (generated with --quick)

from typing import Any, List, Union

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
    def put_input(self, ctx, result = ..., status = ...) -> None: ...
    def put_loading_summary(self, total_duration = ...) -> None: ...
    def put_output(self, output, process_time, status) -> None: ...
    def put_output_summary(self, inputs, files, total_duration) -> None: ...
    def put_total(self, total_duration = ...) -> None: ...
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

class MetricsSimple(AbstractMetricCollector):
    __doc__: str
    _lock: threading.Lock
    _stats: List[str]
    conf: Any

def configure(conf) -> None: ...
