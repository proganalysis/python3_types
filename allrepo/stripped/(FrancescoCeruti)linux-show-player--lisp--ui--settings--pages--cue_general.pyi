# (generated with --quick)

from typing import Any, Dict

CueAction: Any
CueNextAction: Any
CueSettingsPage: Any
FadeComboBox: Any
FadeEdit: Any
QComboBox: Any
QDoubleSpinBox: Any
QGroupBox: Any
QHBoxLayout: Any
QLabel: Any
QT_TRANSLATE_NOOP: Any
QTabWidget: Any
QVBoxLayout: Any
QWidget: Any
Qt: Any
translate: Any

class CueGeneralSettings(Any):
    Name: Any
    fadeInEdit: Any
    fadeInGroup: Any
    fadeOutEdit: Any
    fadeOutGroup: Any
    nextActionCombo: Any
    nextActionGroup: Any
    postWaitGroup: Any
    postWaitLabel: Any
    postWaitSpin: Any
    preWaitGroup: Any
    preWaitLabel: Any
    preWaitSpin: Any
    startActionCombo: Any
    startActionGroup: Any
    startActionLabel: Any
    stopActionCombo: Any
    stopActionGroup: Any
    stopActionLabel: Any
    tabWidget: Any
    tab_1: Any
    tab_2: Any
    tab_3: Any
    def __init__(self, cue_class, **kwargs) -> None: ...
    def enable_check(self, enable) -> None: ...
    def get_settings(self) -> Dict[str, Any]: ...
    def load_settings(self, settings) -> None: ...
    def retranslateUi(self) -> None: ...
