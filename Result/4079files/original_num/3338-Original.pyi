# (generated with --quick)

from typing import Any

COMMAND_NAME: Any
argparse: module
c: HelpCategories
cmd2: Any
sys: module

class HelpCategories(Any):
    CMD_CAT_APP_MGMT: str
    CMD_CAT_CONNECTING: str
    CMD_CAT_SERVER_INFO: str
    __doc__: str
    do_disable_commands: Any
    do_enable_commands: Any
    do_restart: Any
    do_which: Any
    restart_parser: argparse.ArgumentParser
    def __init__(self) -> None: ...
    def do_config(self, _) -> None: ...
    def do_connect(self, _) -> None: ...
    def do_deploy(self, _) -> None: ...
    def do_expire(self, _) -> None: ...
    def do_findleakers(self, _) -> None: ...
    def do_list(self, _) -> None: ...
    def do_redeploy(self, _) -> None: ...
    def do_resources(self, _) -> None: ...
    def do_serverinfo(self, _) -> None: ...
    def do_sessions(self, _) -> None: ...
    def do_sslconnectorciphers(self, _) -> None: ...
    def do_start(self, _) -> None: ...
    def do_status(self, _) -> None: ...
    def do_stop(self, _) -> None: ...
    def do_thread_dump(self, _) -> None: ...
    def do_undeploy(self, _) -> None: ...
    def do_version(self, _) -> None: ...
    def do_vminfo(self, _) -> None: ...
