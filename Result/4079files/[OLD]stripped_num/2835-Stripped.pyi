# (generated with --quick)

from typing import Any
import ui.ui_about_dlg

QDialog: Any
QPixmap: Any
QSize: Any
WndUtils: Any
os: module
pyqtSlot: Any
sys: module
ui_about_dlg: module

class AboutDlg(Any, ui.ui_about_dlg.Ui_AboutDlg, Any):
    app_version_str: Any
    on_btnClose_clicked: Any
    def __init__(self, parent, app_version_str) -> None: ...
    def setupUi(self) -> None: ...
