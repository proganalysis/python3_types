# (generated with --quick)

from typing import Any, List

Transition: Any
__all__: List[str]
abc: module
gym: module

class Environment(metaclass=abc.ABCMeta):
    __doc__: str
    action_space: Any
    last_reward: Any
    observation: Any
    observation_space: Any
    terminated: Any
    @abstractmethod
    def execute(self, action) -> Any: ...
    @abstractmethod
    def reset(self) -> Any: ...
