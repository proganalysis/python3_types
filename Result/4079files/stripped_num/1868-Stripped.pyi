# (generated with --quick)

from typing import Any, Dict, Tuple

FileBackedPlaylist: Any
GObject: Any
GetPlaylistName: Any
Gtk: Any
Icons: Any
PLAYLISTS: Any
Pango: Any
Playlist: Any
SeparatorMenuItem: Any
_: Any
app: Any
get_menu_item_top_parent: Any
ngettext: Any
qltk: Any

class ConfirmMultipleSongsAction(Any):
    ADD: int
    REMOVE: int
    __doc__: str
    def __init__(self, parent, playlist, songs) -> None: ...

class PlaylistMenu(Any):
    __gsignals__: Dict[str, Tuple[Any, None, Tuple[type]]]
    def __init__(self, songs, playlists) -> None: ...
    def _emit_new(self, playlist) -> None: ...
    def _get_new_name(self, parent, title) -> Any: ...
    def _on_new_playlist_activate(self, item, songs) -> None: ...
    def _on_toggle_playlist_activate(self, item, playlist, songs) -> None: ...
