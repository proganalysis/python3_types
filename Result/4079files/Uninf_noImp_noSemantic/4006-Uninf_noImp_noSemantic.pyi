from .security import AdminSecurityMixin
from flask_admin.contrib.sqla import ModelView as BaseModelView
from typing import Any

EXTEND_BASE_CLASS_ATTRIBUTES: Any

class ModelAdmin(AdminSecurityMixin, BaseModelView):
    can_view_details: bool = ...
    menu_icon_type: Any = ...
    menu_icon_value: Any = ...
    create_template: str = ...
    details_template: str = ...
    edit_template: str = ...
    list_template: str = ...
    column_exclude_list: Any = ...
    form_excluded_columns: Any = ...
    column_type_formatters: Any = ...
    column_formatters: Any = ...
    form_base_class: Any = ...
    model_form_converter: Any = ...
    def __getattribute__(self, item: Any): ...