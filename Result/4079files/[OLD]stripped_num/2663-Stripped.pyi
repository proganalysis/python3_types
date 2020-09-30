# (generated with --quick)

from typing import Any, Dict

Application: Any
Cue: Any
CueAction: Any
CueActionComboBox: Any
CueSettingsRegistry: Any
Property: Any
QCheckBox: Any
QComboBox: Any
QGridLayout: Any
QGroupBox: Any
QLabel: Any
QSpinBox: Any
QT_TRANSLATE_NOOP: Any
QVBoxLayout: Any
Qt: Any
SettingsPage: Any
translate: Any

class IndexActionCue(Any):
    Name: Any
    action: Any
    name: Any
    relative: Any
    target_index: Any
    def __init__(self, **kwargs) -> None: ...
    def __start__(self, fade = ...) -> None: ...

class IndexActionCueSettings(Any):
    Name: Any
    _cue_index: Any
    _target_class: Any
    actionCombo: Any
    actionGroup: Any
    indexGroup: Any
    relativeCheck: Any
    targetIndexLabel: Any
    targetIndexSpin: Any
    def __init__(self, **kwargs) -> None: ...
    def _relative_changed(self) -> None: ...
    def _update_action_combo(self) -> None: ...
    def enable_check(self, enabled) -> None: ...
    def get_settings(self) -> Dict[str, Any]: ...
    def load_settings(self, settings) -> None: ...
    def retranslateUi(self) -> None: ...
