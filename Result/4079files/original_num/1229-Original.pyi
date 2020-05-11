# (generated with --quick)

from typing import Any, Dict, List, NoReturn, Optional

BasicTimePicker: Any
JqueryUIDatePicker: Any
Keys: Any
NoSuchElementException: Any
TimeNotBookableError: Any
WebDriverException: Any
datetime: module
elem_has_class: Any
format_dt: Any
logger: logging.Logger
logging: module
os: module
parser: module
re: module
wait_for: Any
webbrowser: module

class RestaurantPageAvailabilityForm:
    _submitted_at: Optional[datetime.datetime]
    availability_check_submit_selector: str
    availability_submit: Any
    available_times: List[datetime.datetime]
    browser: Any
    current_date: datetime.datetime
    date_input_element: Any
    date_input_id: str
    date_input_real_selector: str
    date_input_selector: str
    has_fetched: bool
    loading_overlay_displayed: Any
    loading_overylay_selector: str
    name: Any
    party_size_id: str
    party_size_select_selector: str
    time_select_id: str
    time_select_selector: str
    url: str
    def __init__(self, url: str, browser, implicit_wait: int = ...) -> None: ...
    def _form_nudge(self, trigger_selector) -> None: ...
    def check_has_fetched(self) -> NoReturn: ...
    def find_availability_for(self, dt: datetime.datetime, party_size: int, breakfast = ..., lunch = ..., dinner = ..., any_time = ...) -> Dict[str, Any]: ...
    def get(self) -> None: ...
    def get_datepicker(self) -> Any: ...
    def set_breakfast(self) -> None: ...
    def set_date(self, dt: datetime.datetime) -> None: ...
    def set_dinner(self) -> None: ...
    def set_lunch(self) -> None: ...
    def set_partysize(self, size: int) -> None: ...
    def set_time(self, dt: datetime.datetime) -> None: ...
    def submit_availability_check(self) -> None: ...
