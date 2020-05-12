import urwid
from . import mixins
from typing import Any

class ProjectDetailHeader(mixins.NonSelectableMixin, urwid.WidgetWrap):
    title: Any = ...
    projects_button: Any = ...
    account_button: Any = ...
    def __init__(self, project: Any) -> None: ...
