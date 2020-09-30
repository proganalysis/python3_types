# (generated with --quick)

import tkinter
import tkinter.ttk
import types
from typing import Any, List, Optional, Type

ACTIVE: Any
ALL: Any
ANCHOR: Any
ARC: Any
BASELINE: Any
BEVEL: Any
BOTH: Any
BOTTOM: Any
BROWSE: Any
BUTT: Any
BaseWidget: Type[tkinter.BaseWidget]
BitmapImage: Type[tkinter.BitmapImage]
BooleanVar: Type[tkinter.BooleanVar]
Button: Type[tkinter.ttk.Button]
CASCADE: Any
CENTER: Any
CHAR: Any
CHECKBUTTON: Any
CHORD: Any
COMMAND: Any
CURRENT: Any
CallWrapper: Type[tkinter.CallWrapper]
Canvas: Type[tkinter.Canvas]
Checkbutton: Type[tkinter.ttk.Checkbutton]
Combobox: Type[tkinter.ttk.Combobox]
DISABLED: Any
DOTBOX: Any
DoubleVar: Type[tkinter.DoubleVar]
E: Any
END: Any
EW: Any
EXCEPTION: Any
EXTENDED: Any
Entry: Type[tkinter.ttk.Entry]
Event: Type[tkinter.Event]
FALSE: Any
FIRST: Any
FLAT: Any
Frame: Type[tkinter.ttk.Frame]
GROOVE: Any
GUI_Overlay: module
Grid: Type[tkinter.Grid]
HIDDEN: Any
HORIZONTAL: Any
INSERT: Any
INSIDE: Any
Image: Type[tkinter.Image]
IntVar: Type[tkinter.IntVar]
LAST: Any
LEFT: Any
Label: Type[tkinter.ttk.Label]
LabelFrame: Any
LabeledScale: Type[tkinter.ttk.LabeledScale]
Labelframe: Type[tkinter.ttk.Labelframe]
Listbox: Type[tkinter.Listbox]
MITER: Any
MOVETO: Any
MULTIPLE: Any
Menu: Type[tkinter.Menu]
Menubutton: Type[tkinter.ttk.Menubutton]
Message: Type[tkinter.Message]
Misc: Type[tkinter.Misc]
N: Any
NE: Any
NO: Any
NONE: Any
NORMAL: Any
NS: Any
NSEW: Any
NUMERIC: Any
NW: Any
Notebook: Type[tkinter.ttk.Notebook]
OFF: Any
ON: Any
OUTSIDE: Any
OptionMenu: Type[tkinter.ttk.OptionMenu]
PAGES: Any
PIESLICE: Any
PROJECTING: Any
Pack: Type[tkinter.Pack]
PanedWindow: Any
Panedwindow: Type[tkinter.ttk.Panedwindow]
PhotoImage: Type[tkinter.PhotoImage]
Place: Type[tkinter.Place]
Progressbar: Type[tkinter.ttk.Progressbar]
PunishWindow: Any
RADIOBUTTON: Any
RAISED: Any
READABLE: Any
RIDGE: Any
RIGHT: Any
ROUND: Any
Radiobutton: Type[tkinter.ttk.Radiobutton]
S: Any
SCROLL: Any
SE: Any
SEL: Any
SEL_FIRST: Any
SEL_LAST: Any
SEPARATOR: Any
SINGLE: Any
SOLID: Any
SUNKEN: Any
SW: Any
Scale: Type[tkinter.ttk.Scale]
Scrollbar: Type[tkinter.ttk.Scrollbar]
Separator: Type[tkinter.ttk.Separator]
Sizegrip: Type[tkinter.ttk.Sizegrip]
SoundPlayer: module
Spinbox: Type[tkinter.Spinbox]
StringVar: Type[tkinter.StringVar]
Style: Type[tkinter.ttk.Style]
TOP: Any
TRUE: Any
TclError: Any
TclVersion: Any
Text: Type[tkinter.Text]
Tk: Type[tkinter.Tk]
TkVersion: Any
Toplevel: Type[tkinter.Toplevel]
TracebackType: Type[types.TracebackType]
Treeview: Type[tkinter.ttk.Treeview]
UNDERLINE: Any
UNITS: Any
VERTICAL: Any
Variable: Type[tkinter.Variable]
W: Any
WORD: Any
WRITABLE: Any
Widget: Type[tkinter.ttk.Widget]
Wm: Type[tkinter.Wm]
X: Any
XView: Type[tkinter.XView]
Y: Any
YES: Any
YView: Type[tkinter.YView]
getdouble: Any
getint: Any
wantobjects: Any

class GUI_PunishCoashOverlay(GUI_Overlay.Overlay):
    border_tag: str
    canvas: tkinter.Canvas
    coach_tag: str
    current_window: Any
    frames_since_new_window: int
    has_played_sound: bool
    launcher: Any
    redirector: TextRedirector
    stored_cancels: List[nothing]
    stored_inputs: List[nothing]
    def __init__(self, master, launcher) -> None: ...
    def get_canvas_border_color_by_punish(self) -> Optional[str]: ...
    def play_sound_by_punish(self) -> None: ...
    def set_canvas_border_colors(self, color1, color2) -> None: ...
    def set_canvas_border_to_flash(self) -> None: ...
    def set_canvas_border_to_punish_indicator(self) -> None: ...

class TextRedirector(object):
    def __init__(self, canvas, height) -> None: ...
    def write(self, str) -> None: ...

def NoDefaultRoot() -> Any: ...
def Tcl(screenName = ..., baseName = ..., className: str = ..., useTk: bool = ...) -> Any: ...
def getboolean(s) -> Any: ...
def image_names() -> Any: ...
def image_types() -> Any: ...
def mainloop(n: int = ...) -> Any: ...
def setup_master(master = ...) -> Any: ...
def tclobjs_to_py(adict) -> Any: ...
