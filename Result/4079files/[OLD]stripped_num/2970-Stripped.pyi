# (generated with --quick)

import json.decoder
from typing import Any, Dict, List, Type

HttpLocust: Any
JSONDecodeError: Type[json.decoder.JSONDecodeError]
TaskSet: Any
random: module
reverse: Any
task: Any

class SolvingTaskBehavior(Any):
    SOLVE_PROBABILITY: float
    __doc__: str
    edit_program: Any
    run_program: Any
    task_session_id: Any
    def on_start(self) -> None: ...
    def start_task(self, task_name) -> None: ...

class UserBehavior(Any):
    __doc__: str
    action_urls: Dict[str, Any]
    cookies: dict
    task_names: Any
    tasks: List[Type[SolvingTaskBehavior]]
    def __init__(self, parent) -> None: ...
    @staticmethod
    def log_errors(response) -> None: ...
    def on_start(self) -> None: ...
    def post_with_cookies(self, url, data) -> Any: ...
    def save_action_urls(self) -> None: ...
    def save_cookies(self, response) -> None: ...
    def save_tasks(self) -> None: ...
    def visit_homepage(self) -> Any: ...

class WebsiteUser(Any):
    max_wait: int
    min_wait: int
    task_set: Type[UserBehavior]
