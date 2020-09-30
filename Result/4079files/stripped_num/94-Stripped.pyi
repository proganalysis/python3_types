# (generated with --quick)

from typing import Any

RandomPolicy: Any
np: module
util: Any

class FunkyReward:
    def __call__(self, obs, act, next_obs, *, steps = ...) -> Any: ...

def test_reward_overwrite() -> None: ...
