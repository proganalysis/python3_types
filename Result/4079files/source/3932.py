import abc
from typing import Any

import gym

from demeter.rl.common.transition import Transition

__all__ = ['Environment']


class Environment(metaclass=abc.ABCMeta):
    """An environment with which an agent can interact."""

    @property
    @abc.abstractmethod
    def observation(self) -> Any:
        """The current observation from this environment."""
        pass

    @property
    @abc.abstractmethod
    def last_reward(self) -> float:
        """The last reward received during the last environment transition. 0 if no transitions have occurred."""
        pass

    @property
    @abc.abstractmethod
    def terminated(self) -> bool:
        """
        True if the environment is in a terminal state from which no more action is allowed.

        Use the reset method to reset the environment to a non-terminal state.
        """
        pass

    @property
    @abc.abstractmethod
    def action_space(self) -> gym.Space:
        """The action space of the environment."""
        pass

    @property
    @abc.abstractmethod
    def observation_space(self) -> gym.Space:
        """The observation space of the environment."""
        pass

    @abc.abstractmethod
    def execute(self, action: Any) -> Transition:
        """Execute action in this environment and return a Transition specifying the result."""
        pass

    @abc.abstractmethod
    def reset(self) -> None:
        """Reset this environment to a non-terminal state. Blocks until the operation is complete."""
        pass
