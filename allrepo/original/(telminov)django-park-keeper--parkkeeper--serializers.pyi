# (generated with --quick)

from typing import Any

models: Any
serializers: Any

class Host(Any):
    Meta: type

class HostGroup(Any):
    Meta: type
    hosts: Any

class Monit(Any):
    Meta: type

class MonitSchedule(Any):
    Meta: type
    all_hosts: Any
    monit: Monit
    def get_all_hosts(self, obj) -> list: ...

class Work(Any):
    Meta: type

class WorkSchedule(Any):
    Meta: type
    all_hosts: Any
    work: Work
    def get_all_hosts(self, obj) -> list: ...
