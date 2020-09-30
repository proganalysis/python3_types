# (generated with --quick)

import devices
import method_proxy
import spinner
from typing import Any, Callable, Dict, Type
import updater

Animation: Any
App: Any
BooleanProperty: Any
Clock: Any
Factory: Any
FlashState: Type[updater.FlashState]
Label: Any
MDSpinner: Type[spinner.MDSpinner]
MethodWrapperProxy: Type[method_proxy.MethodWrapperProxy]
NumericProperty: Any
ObjectProperty: Any
Popup: Any
StringProperty: Any
USBDeviceConnection: Type[devices.USBDeviceConnection]
UpdaterEvents: Any
Widget: Any
Window: Any
create_threaded_controller: Any
kivy: Any
os: module
semver: Any
sys: module
threading: module
webbrowser: module

class ConnectedDevice(Any):
    __doc__: str
    bar: Any
    button_state_details: Dict[Any, str]
    controller: Any
    device: Any
    device_opacity: Any
    device_version: Any
    electron_upgrade_popup: Any
    existing_version: Any
    go: Any
    go_text: Any
    in_progress: Any
    making_progress: Any
    progress: Any
    text: Any
    update_state: Any
    update_version: Any
    upgrade_available: Any
    def __init__(self, **kwargs) -> None: ...
    def _can_upgrade(self, device, device_version) -> bool: ...
    def device_changed(self) -> None: ...
    def firmware_version(self) -> Any: ...
    def inactivity(self, dt) -> None: ...
    def on_device(self, instance, value) -> None: ...
    def on_progress(self, instance, value) -> None: ...
    def on_update_state(self, instance, value) -> None: ...
    def on_update_version(self, instance, value) -> None: ...
    def show_upgrade_electron_help(self) -> None: ...
    def start(self) -> None: ...
    def update_button(self) -> None: ...

class FlashView(Any):
    root: ConnectedDevice
    def __init__(self, root: ConnectedDevice) -> None: ...
    def connected_device_changed(self, device) -> None: ...
    def device_version(self, version) -> None: ...
    def error(self, error) -> None: ...
    def progress(self, min, max, current) -> None: ...
    def updater_state_changed(self, state: updater.FlashState) -> None: ...

class Gui(Any):
    icon: str
    thread: threading.Thread
    title: str
    def __init__(self, *args, **kwargs) -> None: ...
    def build(self) -> ConnectedDevice: ...
    def on_pause(self) -> bool: ...

def kivy_event_thread_dispatch(proxy, target, name, f) -> Callable: ...
def large(s) -> str: ...
def post_to_event_thread(target) -> method_proxy.MethodWrapperProxy: ...
def setup_working_dir() -> None: ...
