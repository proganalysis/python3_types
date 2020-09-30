# (generated with --quick)

from typing import Any, Dict, List, Tuple, Union

AbstractAnswer: Any
AbstractTask: Any
CASCADE: Any
DateTimeField: Any
Document: Any
LongField: Any
ObjectId: Any
ReferenceField: Any
StringField: Any
User: Any
__all__: List[str]

class WorkSession(Any):
    __doc__: str
    activity: Any
    answer: Any
    end_time: Any
    meta: Dict[str, Union[bool, str, List[Union[str, Tuple[str, str]]]]]
    start_time: Any
    task: Any
    task_type: Any
    user: Any
    @classmethod
    def get_total_user_time_approximate(cls, user_id) -> int: ...
    @classmethod
    def get_total_user_time_precise(cls, user_id) -> int: ...
