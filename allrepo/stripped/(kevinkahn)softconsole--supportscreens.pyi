# (generated with --quick)

from typing import Any, Dict, List, Tuple, Type

ConsoleDetail: Any
ManualKeyDesc: Type[toucharea.ManualKeyDesc]
TouchPoint: Type[toucharea.TouchPoint]
debug: module
draw: Any
fonts: module
functools: module
hw: module
logsupport: Any
pygame: Any
screen: module
screens: module
screenutil: module
toucharea: module
utilities: module

class ListChooserSubScreen(screen.ScreenDesc):
    BackgroundColor: Any
    CharColor: Any
    DullKeyColor: Tuple[Any, Any, Any]
    Keys: Dict[str, toucharea.TouchPoint]
    ListKeySlots: Dict[str, toucharea.TouchPoint]
    NumSlots: Any
    SlotItem: List[str]
    SlotsVPos: list
    SrcNext: Tuple[Any, Any]
    SrcPrev: Tuple[Any, Any]
    firstitem: Any
    itemlist: Any
    masterscreen: Any
    selection: Any
    sourceheight: Any
    def DisplayListSelect(self) -> None: ...
    def Initialize(self, itemlist) -> None: ...
    def PickItem(self, slotnum) -> None: ...
    def PickItemOK(self, doit) -> None: ...
    def PrevNext(self, nxt) -> None: ...
    def Result(self, _1) -> Any: ...
    def __init__(self, masterscreen, choosername, slots, screenhgt, voffset, proc) -> None: ...

class ValueChangeScreen(screen.ScreenDesc):
    BackgroundColor: Any
    CharColor: Any
    Keys: Dict[str, toucharea.TouchPoint]
    Outline: Any
    Value: Any
    arrowht: int
    arrowwd: Any
    changevals: Any
    chgval: List[Tuple[Tuple[Any, Any], Any]]
    dnarrow: List[list]
    dnarrowcenter: List[Tuple[Any, Any]]
    dnarrowverts: List[List[nothing]]
    font: Any
    initvalue: Any
    label: Any
    labelloc: Tuple[Any, Any]
    labelrend: Any
    name: str
    returnscreen: Any
    setvalueproc: Any
    titlecenter: Tuple[Any, Any]
    uparrow: List[list]
    uparrowcenter: List[Tuple[Any, Any]]
    uparrowverts: List[List[nothing]]
    def AcceptChange(self) -> None: ...
    def CancelChange(self) -> None: ...
    def ValChange(self, delta) -> None: ...
    def __init__(self, BackgroundColor, Outline, CharColor, label, initvalue, changevals, setvalueproc, returnscreen) -> None: ...
    @staticmethod
    def offsetpoint(center, point) -> Tuple[Any, Any]: ...

class VerifyScreen(screen.BaseKeyScreenDesc):
    CallingScreen: Any
    DefaultNavKeysShowing: bool
    DimTO: int
    HubInterestList: Any
    NavKeysShowing: bool
    PersistTO: int
    label: Any
    @staticmethod
    def DefaultNo() -> None: ...
    def Invoke(self) -> None: ...
    def ShowScreen(self) -> None: ...
    def __init__(self, key, gomsg, nogomsg, procyes, procno, callingscreen, bcolor, keycoloroff, charcolor, state, interestlist) -> None: ...

def _TriangleCorners(c, hgt, invert) -> Tuple[Tuple[Any, Any], Tuple[Any, Any], Tuple[Any, Any]]: ...
def wc(clr, factor = ..., layercolor = ...) -> Tuple[Any, Any, Any]: ...
