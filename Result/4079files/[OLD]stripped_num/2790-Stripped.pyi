# (generated with --quick)

from typing import Any, Dict, List, Optional, Type

Category: Any
Location: Any
Report: Any
Visit: Any
all_categories: Any
app: Any
datetime: Type[datetime.datetime]
db: Any
desc: Any
json: module
lazy_gettext: Any

class DropPoint(Any):
    __doc__: str
    category: Any
    category_id: Any
    description: Any
    description_with_level: Any
    history: List[Dict[str, Any]]
    last_report: Any
    last_state: Any
    last_visit: Any
    lat: Any
    level: Any
    lng: Any
    location: Any
    locations: Any
    new_report_count: Any
    new_reports: Any
    number: Any
    priority: float
    priority_base_time: Any
    priority_factor: Any
    removed: Any
    reports: Any
    time: Any
    total_report_count: Any
    visit_interval: Any
    visits: Any
    def __init__(self, number, category_id = ..., description = ..., lat = ..., lng = ..., level = ..., time = ...) -> None: ...
    def __repr__(self) -> str: ...
    @classmethod
    def get_dp_info(cls, number) -> Optional[Dict[str, Any]]: ...
    @classmethod
    def get_dp_json(cls, number) -> str: ...
    @staticmethod
    def get_dps_json(time = ...) -> str: ...
    @staticmethod
    def get_next_free_number() -> Any: ...
    def remove(self, time = ...) -> None: ...
    def report(self, state = ..., time = ...) -> None: ...
    def visit(self, action = ..., time = ...) -> None: ...
