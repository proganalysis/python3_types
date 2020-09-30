# (generated with --quick)

from typing import Any, List, Optional, Tuple, TypeVar

QtCore: Any
QtWidgets: Any
wb_main_window: module
wb_table_view: module
wb_tracked_qwidget: module

_T0 = TypeVar('_T0')

class WbAnnotateModel(Any):
    all_annotation_nodes: Any
    all_commit_log_nodes: Any
    app: Any
    col_author: int
    col_date: int
    col_line_num: int
    col_line_text: int
    col_revision: int
    column_titles: Tuple[str, str, str, str, str]
    debugLog: Any
    fixed_font: Any
    def __init__(self, app) -> None: ...
    def annotationLogNode(self, rev_num) -> None: ...
    def annotationNode(self, row) -> Any: ...
    def columnCount(self, parent) -> int: ...
    def data(self, index, role) -> Any: ...
    def headerData(self, section, orientation, role) -> Any: ...
    def loadAnnotationForFile(self, all_annotation_nodes, all_commit_log_nodes) -> None: ...
    def rowCount(self, parent) -> int: ...

class WbAnnotateTableView(wb_table_view.WbTableView):
    debugLog: Any
    main_window: Any
    def __init__(self, main_window) -> None: ...
    def selectionChanged(self, selected, deselected) -> None: ...

class WbAnnotateView(wb_main_window.WbMainWindow, wb_tracked_qwidget.WbTrackedModeless):
    annotate_model: WbAnnotateModel
    annotate_table: WbAnnotateTableView
    app: Any
    commit_message: Any
    current_annotations: Optional[list]
    current_commit_selections: List[nothing]
    current_file_selection: List[nothing]
    debugLog: Any
    ui_component: Any
    v_message_layout: Any
    v_message_widget: Any
    v_split: Any
    def _WbAnnotateView__setupTableContextMenu(self) -> None: ...
    def __init__(self, app, ui_component, title) -> None: ...
    def isScmTypeActive(self, scm_type) -> Any: ...
    def selectionChangedAnnotation(self) -> None: ...
    def setupMenuBar(self, mb) -> None: ...
    def setupToolBar(self) -> None: ...
    def showAnnotationForFile(self, all_annotation_nodes, all_commit_log_nodes) -> None: ...

def U_(s: _T0) -> _T0: ...
