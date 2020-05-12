# (generated with --quick)

from typing import Any

QApplication: Any
QBuffer: Any
QByteArray: Any
QIODevice: Any
QImage: Any
QPainter: Any
QUrl: Any
QWebEngineView: Any
io: module

class Screenshot(Any):
    _loaded: bool
    app: Any
    def __init__(self) -> None: ...
    def _load_finished(self, result) -> None: ...
    def capture(self, url) -> Any: ...
    def wait_load(self) -> None: ...
