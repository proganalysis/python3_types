import abc
import gym
from demeter.rl.common.transition import Transition
from typing import Any

__all__: Any

class Environment(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def observation(self) -> Any: ...
    @property
    @abc.abstractmethod
    def last_reward(self) -> float: ...
    @property
    @abc.abstractmethod
    def terminated(self) -> bool: ...
    @property
    @abc.abstractmethod
    def action_space(self) -> gym.Space: ...
    @property
    @abc.abstractmethod
    def observation_space(self) -> gym.Space: ...
    @abc.abstractmethod
    def execute(self, action: Any) -> Transition: ...
    @abc.abstractmethod
    def reset(self) -> None: ...
