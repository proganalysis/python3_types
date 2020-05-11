# (generated with --quick)

from typing import Any, Dict, Optional

DU_CRF_Task: Any
GraphSkewedCut_H_lines: Any
My_FeatureDefinition_v3: Any
NodeType_BIESO_to_BIO_Shape: Any
NodeType_PageXml_Cut_Shape: Any
ShapeLoader: Any
TranskribusDU_version: Any
etree: Any
main_command_line: Any
os: module
shapely: Any
sys: module
traceln: Any

class DU_ABPTableSkewedRowCutLine(Any):
    __doc__: str
    bCutAbove: Any
    fCutHeight: Any
    iBlockVisibility: Any
    iLineVisibility: Any
    lRadAngle: Any
    sXmlFilenamePattern: str
    def __init__(self, sModelName, sModelDir, iBlockVisibility = ..., iLineVisibility = ..., fCutHeight = ..., bCutAbove = ..., lRadAngle = ..., sComment = ..., C = ..., tol = ..., njobs = ..., max_iter = ..., inference_cache = ...) -> None: ...
    @classmethod
    def getConfiguredGraphClass(cls) -> Any: ...

class NodeType_BIESO_to_SIOStSmSb_Shape(Any):
    __doc__: str
    bColumnHeader: bool
    dConverter: Dict[str, Optional[str]]
    def parseDomNodeLabel(self, domnode, defaultCls = ...) -> Any: ...
