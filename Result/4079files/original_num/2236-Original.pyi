# (generated with --quick)

from typing import Any

IgnoreList: Any
collections: module
itertools: module
worker: Any

class RequestsPool(object):
    __doc__: str
    _blacklisted_requests: set
    _requests_storage: Any
    _time_conflicting_requests: set
    _time_relevant_requests: set
    activity_list: list
    current_activities_requests: set
    ignore_list: Any
    make_groups: Any
    pairs: collections.defaultdict[nothing, list]
    req_by_activities: collections.defaultdict
    def __init__(self, storage) -> None: ...
    def _filter_ignored(self, combinations) -> list: ...
    @staticmethod
    def _filter_uniques(combinations) -> list: ...
    def _set_time_conflicting_requests(self) -> None: ...
    def _update_activity_list(self) -> None: ...
    def update_requests_from_storage(self) -> None: ...
