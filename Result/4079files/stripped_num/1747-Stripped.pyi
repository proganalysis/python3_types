# (generated with --quick)

import threading
from typing import Any, Type

Contest: Any
Problem: Any
REJUDGE_COUNTER: str
REJUDGE_TASK_LIMIT: int
SubmissionStatus: Any
Thread: Type[threading.Thread]
async_task: Any
cache: Any
judge_submission_on_contest: Any
judge_submission_on_problem: Any
transaction: Any

def rejudge_all_submission_on_contest(contest) -> None: ...
def rejudge_all_submission_on_contest_problem(contest, problem) -> None: ...
def rejudge_all_submission_on_problem(problem) -> None: ...
def rejudge_submission(submission, callback = ..., run_until_complete = ...) -> None: ...
def rejudge_submission_set(submission_set) -> None: ...
def sleep(secs: float) -> None: ...
