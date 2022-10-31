import torch
from allennlp.common.from_params import FromParams
from allennlp.models.model import Model
from typing import Any, Callable, Optional, Set

logger: Any

class TensorboardWriter(FromParams):
    _train_log: Any = ...
    _validation_log: Any = ...
    _summary_interval: Any = ...
    _histogram_interval: Any = ...
    _should_log_parameter_statistics: Any = ...
    _should_log_learning_rate: Any = ...
    _get_batch_num_total: Any = ...
    def __init__(self, get_batch_num_total: Callable[[], int], serialization_dir: Optional[str]=..., summary_interval: int=..., histogram_interval: int=..., should_log_parameter_statistics: bool=..., should_log_learning_rate: bool=...) -> None: ...
    @staticmethod
    def _item(value: Any) -> Any: ...
    def should_log_this_batch(self) -> bool: ...
    def should_log_histograms_this_batch(self) -> bool: ...
    def add_train_scalar(self, name: str, value: float, timestep: int=...) -> None: ...
    def add_train_histogram(self, name: str, values: torch.Tensor) -> None: ...
    def add_validation_scalar(self, name: str, value: float, timestep: int=...) -> None: ...
    def log_parameter_and_gradient_statistics(self, model: Model, batch_grad_norm: float) -> None: ...
    def log_learning_rates(self, model: Model, optimizer: torch.optim.Optimizer) -> Any: ...
    def log_histograms(self, model: Model, histogram_parameters: Set[str]) -> None: ...
    def log_metrics(self, train_metrics: dict, val_metrics: dict=..., epoch: int=..., log_to_console: bool=...) -> None: ...
    def enable_activation_logging(self, model: Model) -> None: ...
    def log_activation_histogram(self, outputs: Any, log_prefix: str) -> None: ...
    def close(self) -> None: ...