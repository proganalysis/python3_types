# (generated with --quick)

from typing import Any

Config: Any
Countdown: Any
Events: Any
Graph: Any
Gtk: Any
HeaderBar: Any
Session: Any
ShortcutManager: Any
SingletonScope: Any
State: Any
TaskButton: Any
TrayIcon: Any
UI: Any
pytest: Any
random: module
scan_to_graph: Any
shortcut_manager: Any
subject: Any
task_button: Any

class TestHide:
    def test_should_hide_in_tray_when_a_tray_plugin_is_enabled(self, subject) -> None: ...
    def test_should_minimize_when_none_tray_plugin_is_enabled(self, subject) -> None: ...

class TestInitialize:
    def test_should_initialize_shortcuts_and_session_buttons(self, subject, task_button, shortcut_manager) -> None: ...

class TestQuit:
    def test_should_hide_when_timer_is_running(self, subject, mocker) -> None: ...
    def test_should_quit_when_timer_is_not_running(self, mocker, subject) -> None: ...

class TestRun:
    def test_should_call_gtk_main(self, mocker, subject) -> None: ...

class TestShow:
    def test_should_present_window(self, subject, mocker) -> None: ...

def test_interface_compliance(subject) -> None: ...
def test_module(graph) -> None: ...
