# (generated with --quick)

from typing import Any

QGridLayout: Any
QIcon: Any
QIconPushButton: Any
QSize: Any
QSizePolicy: Any
QWidget: Any
Qt: Any
translate: Any

class CueControlButtons(Any):
    fadeInButton: Any
    fadeOutButton: Any
    interruptButton: Any
    pauseButton: Any
    startButton: Any
    stopButton: Any
    def __init__(self, **kwargs) -> None: ...
    def newButton(self, icon) -> Any: ...
    def pauseMode(self) -> None: ...
    def startMode(self) -> None: ...

class ShowControlButtons(Any):
    fadeInButton: Any
    fadeOutButton: Any
    interruptButton: Any
    pauseButton: Any
    resumeButton: Any
    stopButton: Any
    def __init__(self, **kwargs) -> None: ...
    def newButton(self, icon) -> Any: ...
    def retranslateUi(self) -> None: ...
