# (generated with --quick)

from typing import Any

AnsiblePlaybook: Any
CloudUpload: Any
CreateRootIndex: Any
FallibleTask: Any
GzipLogFiles: Any
PopenTask: Any
TaskException: Any
constants: Any
create_file_from_template: Any
logging: module
logging_init_file_handler: Any
os: module
shutil: module
socket: module
subprocess: module
urllib: module
uuid: module
with_vagrant: Any

class Build(JobTask):
    _run: Any
    action_name: str
    description: Any
    git_refspec: Any
    git_repo: Any
    git_version: Any
    link_image: bool
    no_destroy: bool
    pr_author: None
    pr_number: None
    publish_artifacts: bool
    remote_url: str
    repo_owner: None
    returncode: int
    task_name: None
    template_name: Any
    template_version: Any
    timeout: Any
    uuid: str
    def __init__(self, template, git_refspec = ..., git_version = ..., git_repo = ..., timeout = ..., topology = ..., **kwargs) -> None: ...
    def build(self) -> None: ...
    def collect_build_artifacts(self) -> None: ...
    def create_yum_repo(self, base_url = ...) -> None: ...

class JobTask(Any):
    data_dir: Any
    description: str
    link_image: Any
    no_destroy: Any
    pr_author: Any
    pr_number: Any
    publish_artifacts: Any
    remote_url: str
    repo_owner: Any
    returncode: int
    task_name: Any
    template_name: Any
    template_version: Any
    timeout: Any
    uuid: str
    vagrantfile: Any
    def __init__(self, template, no_destroy = ..., publish_artifacts = ..., link_image = ..., pr_number = ..., pr_author = ..., task_name = ..., repo_owner = ..., **kwargs) -> None: ...
    def _after(self) -> None: ...
    def _before(self) -> None: ...
    def compress_logs(self) -> None: ...
    def create_root_index(self) -> None: ...
    def terminate(self) -> None: ...
    def upload_artifacts(self) -> None: ...
    def write_hostname_to_file(self) -> None: ...
    def write_pr_ci_version(self) -> None: ...

class RunADTests(RunPytest):
    action_name: str
    build_url: Any
    description: str
    link_image: bool
    no_destroy: bool
    pr_author: None
    pr_number: None
    publish_artifacts: bool
    remote_url: str
    repo_owner: None
    returncode: int
    task_name: None
    template_name: Any
    template_version: Any
    test_suite: Any
    timeout: Any
    topology_name: Any
    update_packages: Any
    uuid: str
    xmlrpc: Any

class RunPytest(JobTask):
    _run: Any
    action_name: str
    build_url: Any
    description: str
    link_image: bool
    no_destroy: bool
    pr_author: None
    pr_number: None
    publish_artifacts: bool
    remote_url: str
    repo_owner: None
    returncode: int
    run_tests_cmd: str
    task_name: None
    template_name: Any
    template_version: Any
    test_suite: Any
    timeout: Any
    topology_name: Any
    update_packages: Any
    uuid: str
    vagrantfile: Any
    xmlrpc: Any
    def __init__(self, template, build_url, test_suite, topology = ..., timeout = ..., update_packages = ..., xmlrpc = ..., **kwargs) -> None: ...
    def _handle_test_exception(self, exc) -> None: ...
    def execute_tests(self) -> None: ...

class RunPytest2(RunPytest):
    build_url: Any
    description: str
    link_image: bool
    no_destroy: bool
    pr_author: None
    pr_number: None
    publish_artifacts: bool
    remote_url: str
    repo_owner: None
    returncode: int
    run_tests_cmd: str
    task_name: None
    template_name: Any
    template_version: Any
    test_suite: Any
    timeout: Any
    topology_name: Any
    update_packages: Any
    uuid: str
    xmlrpc: Any

class RunPytest3(RunPytest):
    build_url: Any
    description: str
    link_image: bool
    no_destroy: bool
    pr_author: None
    pr_number: None
    publish_artifacts: bool
    remote_url: str
    repo_owner: None
    returncode: int
    run_tests_cmd: str
    task_name: None
    template_name: Any
    template_version: Any
    test_suite: Any
    timeout: Any
    topology_name: Any
    update_packages: Any
    uuid: str
    xmlrpc: Any

class RunWebuiTests(RunPytest):
    action_name: str
    build_url: Any
    description: str
    link_image: bool
    no_destroy: bool
    pr_author: None
    pr_number: None
    publish_artifacts: bool
    remote_url: str
    repo_owner: None
    returncode: int
    task_name: None
    template_name: Any
    template_version: Any
    test_suite: Any
    timeout: Any
    topology_name: Any
    update_packages: Any
    uuid: str
    vagrantfile: Any
    xmlrpc: Any
