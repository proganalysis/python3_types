# (generated with --quick)

from typing import Any

TestCase: Any
User: Any
models: Any

class ModelAnsibleUser(Any):
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...

class ModelHost(Any):
    def setUp(self) -> None: ...
    def test_get_vars(self) -> None: ...
    def test_str(self) -> None: ...

class ModelHostGroup(Any):
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...

class ModelTask(Any):
    user: Any
    def setUp(self) -> None: ...
    def test_ansible_command(self) -> None: ...
    def test_get_duration_date(self) -> None: ...
    def test_get_duration_none(self) -> None: ...
    def test_str(self) -> None: ...

class ModelTaskLog(Any):
    user: Any
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...

class ModelTaskTemplate(Any):
    user: Any
    def setUp(self) -> None: ...
    def test_create_task(self) -> None: ...
    def test_get_hosts_without_group(self) -> None: ...
    def test_str(self) -> None: ...
    def test_uncompleted_task_false(self) -> None: ...
    def test_uncompleted_task_true(self) -> None: ...

class ModelVariable(Any):
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...
