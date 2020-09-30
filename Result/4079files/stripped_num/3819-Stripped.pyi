# (generated with --quick)

from typing import Any, Type

ModuleStorage: Any
admin: Any
forms: Any
json: module

class ModuleStorageAdmin(Any):
    form: Type[ModuleStorageModelForm]
    def save_model(self, request, obj, form, change) -> None: ...

class ModuleStorageModelForm(Any):
    def __init__(self, *args, **kwargs) -> None: ...
    def display_as_lines(self, value) -> str: ...
