# (generated with --quick)

from typing import Any, Dict

AsyncIOHTTPClient: Any
BadResponseError: Any
BaseTestRunner: Any
CoroutineMock: Any
Poller: Any
alertnotify: Any
fake_call: Any
patch: Any
pytest: Any
return_once: Any
setup_proxies: Any

class FakePoller(Any):
    _cmds: Dict[str, Any]
    def __init__(self, blocknotify = ..., walletnotify = ..., alertnotify = ...) -> None: ...

class TestPoller(Any):
    run_with_node: bool
    test_alertnotify_invalid_func_with_error_raise_and_notify: Any
    test_alertnotify_invalid_func_with_error_raise_no_notify: Any
    test_alertnotify_valid_func_without_errors: Any
    test_call_blocknotify_and_has_block: Any
    test_call_blocknotify_and_has_no_block: Any
    test_call_walletnotify_and_has_no_trans: Any
    test_call_walletnotify_and_has_trans: Any
    test_method__build_filter_which_exists: Any
    test_method__build_filter_which_not_exists: Any
    test_method__exec_command_exist_cmd: Any
    test_method__exec_command_no_such_cmd: Any
    test_method__exec_command_some_error: Any
    test_method__is_account_trans_and_trans_exists: Any
    test_method__is_account_trans_and_trans_not_exists: Any
    test_method__poll_with_reconnect_when_droped: Any
    test_method_has_command: Any
