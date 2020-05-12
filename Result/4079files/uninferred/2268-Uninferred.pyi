from rlbot.agents.base_agent import BaseAgent
from typing import Any

class BaseIndependentAgent(BaseAgent):
    def run_independently(self, terminate_request_event: Any) -> None: ...
