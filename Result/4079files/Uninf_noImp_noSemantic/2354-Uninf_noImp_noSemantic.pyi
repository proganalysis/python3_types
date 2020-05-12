from .common import FallibleTask
from typing import Any, Optional

class JobTask(FallibleTask):
    template_name: Any = ...
    template_version: Any = ...
    publish_artifacts: Any = ...
    timeout: Any = ...
    uuid: Any = ...
    remote_url: str = ...
    returncode: int = ...
    no_destroy: Any = ...
    description: str = ...
    link_image: Any = ...
    pr_number: Any = ...
    pr_author: Any = ...
    task_name: Any = ...
    repo_owner: Any = ...
    def __init__(self, template: Any, no_destroy: bool = ..., publish_artifacts: bool = ..., link_image: bool = ..., pr_number: Optional[Any] = ..., pr_author: Optional[Any] = ..., task_name: Optional[Any] = ..., repo_owner: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def vagrantfile(self): ...
    @property
    def data_dir(self): ...
    def compress_logs(self) -> None: ...
    def write_hostname_to_file(self) -> None: ...
    def write_pr_ci_version(self) -> None: ...
    def _before(self) -> None: ...
    def _after(self) -> None: ...
    def upload_artifacts(self) -> None: ...
    def create_root_index(self) -> None: ...
    def terminate(self) -> None: ...

class Build(JobTask):
    action_name: str = ...
    git_refspec: Any = ...
    git_version: Any = ...
    git_repo: Any = ...
    def __init__(self, template: Any, git_refspec: Optional[Any] = ..., git_version: Optional[Any] = ..., git_repo: Optional[Any] = ..., timeout: Any = ..., topology: Optional[Any] = ..., **kwargs: Any) -> None: ...
    returncode: int = ...
    def _run(self) -> None: ...
    description: Any = ...
    def _after(self) -> None: ...
    def build(self) -> None: ...
    def collect_build_artifacts(self) -> None: ...
    def create_yum_repo(self, base_url: Any = ...) -> None: ...

class RunPytest(JobTask):
    action_name: str = ...
    run_tests_cmd: str = ...
    build_url: Any = ...
    test_suite: Any = ...
    update_packages: Any = ...
    xmlrpc: Any = ...
    topology_name: Any = ...
    def __init__(self, template: Any, build_url: Any, test_suite: Any, topology: Optional[Any] = ..., timeout: Any = ..., update_packages: bool = ..., xmlrpc: bool = ..., **kwargs: Any) -> None: ...
    @property
    def vagrantfile(self): ...
    def _before(self) -> None: ...
    returncode: int = ...
    def _run(self) -> None: ...
    def execute_tests(self) -> None: ...
    def _handle_test_exception(self, exc: Any) -> None: ...

class RunPytest2(RunPytest):
    run_tests_cmd: str = ...

class RunPytest3(RunPytest):
    run_tests_cmd: str = ...

class RunWebuiTests(RunPytest):
    action_name: str = ...
    @property
    def vagrantfile(self): ...
    def execute_tests(self) -> None: ...
    def _handle_test_exception(self, exc: Any) -> None: ...

class RunADTests(RunPytest):
    action_name: str = ...
