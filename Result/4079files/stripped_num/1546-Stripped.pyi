# (generated with --quick)

import functools
import threading
from typing import Any, Type

GLib: Any
GObject: Any
Gdk: Any
Gio: Any
Gtk: Any
Pango: Any
Thread: Type[threading.Thread]
Vte: Any
neovim: Any
partial: Type[functools.partial]

class NeovimBufferBar(Any):
    __doc__: str
    bids: list
    btns: list
    nvim_switch_buffer: Any
    updating: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def _do_button_toggled(self, btn) -> None: ...
    def update(self, buflist, bufcurr) -> None: ...

class NeovimTabBar(Any):
    __doc__: str
    nvim_switch_tab: Any
    updating: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def _do_switch_page(self, _, page, num) -> None: ...
    def update(self, tablist, tabcurr) -> None: ...

class NeovimTerminal(Any):
    __doc__: str
    nvim_attached: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def reset_color(self) -> None: ...
    def reset_font(self) -> None: ...
    def spawn(self, addr, argv, rtp) -> None: ...
    def update_color(self, bg_color, is_dark) -> None: ...
    def update_font(self, value) -> None: ...

class NeovimViewport(Any):
    __doc__: str
    lines: Any
    nvim_vscrolled: Any
    updating: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def _do_vadjustment_value_changed(self, vadj) -> None: ...
    def update(self, a, b, lines) -> None: ...

class NeovimWindow(Any):
    __doc__: str
    notebook: NeovimTabBar
    nvim_notify: Any
    nvim_request: Any
    nvim_setup: Any
    switcher: NeovimBufferBar
    terminal: NeovimTerminal
    viewport: NeovimViewport
    def __init__(self, *args, **kwargs) -> None: ...
    def update_clipboard(self, method, data) -> Any: ...
