# (generated with --quick)

import multiprocessing.context
from typing import Any, NoReturn, Type
import unittest.case

EC: Any
Process: Type[multiprocessing.context.Process]
api: Any
configs: Any
json: module
os: module
posts: Any
requests: module
schedulerv2: Any
shutil: module
sync: Any
sys: module
time: module
unittest: module

class TestAPIGunicornScheduler(unittest.case.TestCase):
    api_discovery: str
    app_path: str
    assets_path: str
    dbs_path: str
    inte_path: str
    matchbox_path: str
    p_api: Type[multiprocessing.context.Process]
    p_matchbox: Type[multiprocessing.context.Process]
    project_path: str
    test_matchbox_path: str
    tests_path: str
    def api_healthz(self) -> None: ...
    @staticmethod
    def api_running(api_endpoint, p_api) -> None: ...
    @staticmethod
    def clean_sandbox() -> None: ...
    @staticmethod
    def matchbox_running(matchbox_endpoint, p_matchbox) -> None: ...
    @staticmethod
    def process_target_api() -> NoReturn: ...
    @staticmethod
    def process_target_matchbox() -> NoReturn: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...

class TestEtcdMemberKubernetesControlPlane1(TestAPIGunicornScheduler):
    def test_01(self) -> None: ...

class TestEtcdMemberKubernetesControlPlane2(TestAPIGunicornScheduler):
    def test_02(self) -> None: ...

class TestEtcdMemberKubernetesControlPlane3(TestAPIGunicornScheduler):
    def test_03(self) -> None: ...

class TestEtcdMemberKubernetesControlPlane4(TestAPIGunicornScheduler):
    def test_04(self) -> None: ...
