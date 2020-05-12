from django.test import TestCase
from typing import Any

class ModelVariable(TestCase):
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...

class ModelHostGroup(TestCase):
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...

class ModelHost(TestCase):
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...
    def test_get_vars(self) -> None: ...

class ModelAnsibleUser(TestCase):
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...

class ModelTaskTemplate(TestCase):
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...
    user: Any = ...
    def test_create_task(self) -> None: ...
    def test_uncompleted_task_false(self) -> None: ...
    def test_uncompleted_task_true(self) -> None: ...
    def test_get_hosts_without_group(self) -> None: ...

class ModelTask(TestCase):
    user: Any = ...
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...
    def test_get_duration_date(self) -> None: ...
    def test_get_duration_none(self) -> None: ...
    def test_ansible_command(self) -> None: ...

class ModelTaskLog(TestCase):
    user: Any = ...
    def setUp(self) -> None: ...
    def test_str(self) -> None: ...
