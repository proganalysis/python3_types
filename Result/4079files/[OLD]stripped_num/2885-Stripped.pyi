# (generated with --quick)

import db.database
from typing import Any, Coroutine, List

asyncio: module
commands: Any
database: module
discord: Any
global_methods: module
playlist: module

class Voice:
    add_to_queue: Any
    bot: Any
    database: db.database.Database
    leaveChannel: Any
    music_server: None
    people_voted: List[nothing]
    peter: Any
    play_audio: Any
    play_next: Any
    player: Any
    playlist: playlist.Queue
    print_playlist: Any
    seconds_to_next: Any
    set_volume: Any
    start_queue: Any
    stop_audio: Any
    summon: Any
    time_left: Any
    voice: Any
    volume: float
    vote_next_song: Any
    def __init__(self, bot) -> None: ...
    def get_or_take_member_channel(self, ctx) -> Any: ...
    def get_requested_server(self, ctx) -> Any: ...
    def play_music(self, link) -> Coroutine[Any, Any, None]: ...
    def queue_is_alive(self) -> Coroutine[Any, Any, None]: ...
    def respond(self, msg, author) -> Coroutine[Any, Any, None]: ...

def setup(bot) -> None: ...
