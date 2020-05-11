# (generated with --quick)

from typing import Any, Dict, NoReturn, Type, Union

act_fns: Dict[str, Type[Union[Linear, ReLU, Sigmoid, SoftMax, Sqrt, Tanh]]]
linear: Any
linear_p: Any
relu: Any
relu_p: Any
s1: Any
sigmoid: Any
sigmoid_p: Any
softmax: Any
softmax_p: Any
sqrt: Any
sqrt_p: Any
tanh: Any
tanh_p: Any

class ActivationFunction:
    type: str
    def __call__(self, Z) -> NoReturn: ...
    def __str__(self) -> str: ...
    def derivative(self, Z) -> NoReturn: ...

class Linear(ActivationFunction):
    __call__: Any
    derivative: Any
    type: str

class ReLU(ActivationFunction):
    __call__: Any
    derivative: Any
    type: str

class Sigmoid(ActivationFunction):
    __call__: Any
    derivative: Any
    type: str

class SoftMax(ActivationFunction):
    __call__: Any
    true_derivative: Any
    type: str
    def derivative(self, A) -> Any: ...

class Sqrt(ActivationFunction):
    __call__: Any
    derivative: Any
    type: str

class Tanh(ActivationFunction):
    __call__: Any
    derivative: Any
    type: str
