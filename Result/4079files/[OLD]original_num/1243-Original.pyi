# (generated with --quick)

from typing import Any, Type

croniter: Type[croniter.croniter]
forms: Any
json: module
models: Any

class BaseSchedule(Any):
    def clean(self) -> Any: ...
    def clean_cron(self) -> Any: ...
    def clean_options_json(self) -> Any: ...

class Credential(Any):
    Meta: type
    password: Any
    def clean_password(self) -> Any: ...

class MonitSchedule(Any):
    Meta: type

class WorkSchedule(Any):
    Meta: type
