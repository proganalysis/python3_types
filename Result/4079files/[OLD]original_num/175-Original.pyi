# (generated with --quick)

from typing import Any

Application: Any
Logger: Any
MachineAction: Any
PluginRegistry: Any
QObject: Any
catalog: Any
i18nCatalog: Any
os: module
pyqtProperty: Any
pyqtSignal: Any
pyqtSlot: Any
time: module

class DiscoverUM3Action(Any):
    _DiscoverUM3Action__additional_component: None
    _DiscoverUM3Action__additional_components_context: None
    _DiscoverUM3Action__additional_components_view: Any
    _last_zeroconf_event_time: float
    _network_plugin: None
    _qml_url: str
    _zeroconf_change_grace_period: float
    foundDevices: Any
    getStoredKey: Any
    loadConfigurationFromPrinter: Any
    printersChanged: Any
    removeManualPrinter: Any
    reset: Any
    restartDiscovery: Any
    setKey: Any
    setManualPrinter: Any
    startDiscovery: Any
    def __init__(self) -> None: ...
    def _createAdditionalComponentsView(self) -> None: ...
    def _onPrinterDiscoveryChanged(self, *args) -> None: ...
