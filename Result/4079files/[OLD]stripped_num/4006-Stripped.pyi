# (generated with --quick)

from typing import Any, Callable, Dict, Tuple, Type

AdminSecurityMixin: Any
BaseModelView: Any
CustomAdminConverter: Any
EXTEND_BASE_CLASS_ATTRIBUTES: Tuple[str, str]
ICON_TYPE_GLYPH: Any
ReorderableForm: Any
date: Type[datetime.date]
datetime: Type[datetime.datetime]
macro: Any

class ModelAdmin(Any, Any):
    can_view_details: bool
    column_exclude_list: Tuple[str, str]
    column_formatters: Dict[str, Any]
    column_type_formatters: Dict[Type[datetime.date], Callable[[Any, Any], Any]]
    create_template: str
    details_template: str
    edit_template: str
    form_base_class: Any
    form_excluded_columns: Tuple[str, str]
    list_template: str
    menu_icon_type: Any
    menu_icon_value: None
    model_form_converter: Any
    def __getattribute__(self, item) -> Any: ...
