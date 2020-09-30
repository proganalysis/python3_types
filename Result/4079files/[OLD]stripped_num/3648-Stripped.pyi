# (generated with --quick)

from typing import Any, Iterable, List

Application: Any
ExtruderStack: Any
QTimer: Any
Qt: Any
UM: Any
catalog: Any
i18nCatalog: Any
pyqtProperty: Any
pyqtSignal: Any

class ExtrudersModel(Any):
    ColorRole: Any
    DefinitionRole: Any
    IdRole: Any
    IndexRole: Any
    MaterialRole: Any
    NameRole: Any
    VariantRole: Any
    _ExtrudersModel__updateExtruders: Any
    _active_machine_extruders: Iterable
    _add_optional_extruder: Any
    _simple_names: Any
    _update_extruder_timer: Any
    addOptionalExtruder: Any
    addOptionalExtruderChanged: Any
    defaultColors: List[str]
    modelChanged: Any
    simpleNames: Any
    simpleNamesChanged: Any
    def __init__(self, parent = ...) -> None: ...
    def _extrudersChanged(self, machine_id = ...) -> None: ...
    def _onExtruderStackContainersChanged(self, container) -> None: ...
    def _updateExtruders(self) -> None: ...
    def setAddOptionalExtruder(self, add_optional_extruder) -> None: ...
    def setSimpleNames(self, simple_names) -> None: ...
