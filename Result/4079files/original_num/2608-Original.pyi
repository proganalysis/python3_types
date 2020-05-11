# (generated with --quick)

from typing import Any, Dict, Type

BaseHandler: Any
Database: Any
Validators: Any
datetime: Type[datetime.datetime]
json: module

class InfoHandler(Any):
    get_input: Any
    get_output: Any
    get_source: Any
    get_submission: Any
    get_submissions: Any
    get_user: Any
    def get_contest(self) -> Dict[str, Any]: ...
    @staticmethod
    def patch_output(output) -> Any: ...
    @staticmethod
    def patch_submission(submission) -> Any: ...
