# (generated with --quick)

from typing import Any

Category: Any
FileSystemStorage: Any
ProblemAttachmentStorage: Any
Session: Any
User: Any
get_user_model: Any
models: Any
os: module
settings: Any

class Problem(Any):
    Meta: type
    auth_key: Any
    author: Any
    categories: Any
    description: Any
    last_modified: Any
    title: Any
    def __str__(self) -> str: ...
    def categories_title(self) -> str: ...

class ProblemAttachment(Any):
    Meta: type
    file: Any
    problem: Any
    def __str__(self) -> str: ...
    def filename(self) -> Any: ...

class ProblemAuthLog(Any):
    Meta: type
    auth_key: Any
    datetime: Any
    problem_instance: Any
    user: Any

class ProblemInstance(Any):
    Meta: type
    breakthrough_points: Any
    distributed_points: Any
    hidden: Any
    points: Any
    problem: Any
    problem_list: Any
    def __str__(self) -> str: ...

class ProblemList(Any):
    Meta: type
    allow_question: Any
    announcement: Any
    description: Any
    session: Any
    title: Any
    def __str__(self) -> str: ...

class ProblemQuestion(Any):
    Meta: type
    answer: Any
    datetime: Any
    problem_instance: Any
    question: Any
    user: Any

def upload_target(problem_attachment, filename) -> str: ...
