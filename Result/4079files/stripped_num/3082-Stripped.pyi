# (generated with --quick)

from typing import Any, TypeVar, Union

BaseListView: Any
COULD_BE_STARTUP_CHECK: Any
OrganizationHelper: Any

_T0 = TypeVar('_T0')

class OrganizationListView(Any):
    helper_class: Any
    view_name: str
    def description_check(self, check_name: _T0) -> Union[bool, _T0]: ...
