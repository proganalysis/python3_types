# (generated with --quick)

import event
from typing import Any, Type

Event: Type[event.Event]
app: AppDispatcher
player: PlayerDispatcher
recorder: RecorderDispatcher
storage: StorageDispatcher

class AppDispatcher:
    exit_clicked: Any

class PlayerDispatcher:
    change_station_clicked: Any
    pause_clicked: Any
    play_clicked: Any
    playing_paused: Any
    playing_started: Any
    playing_state_changed: Any
    song_changed: Any
    station_changed: Any

class RecorderDispatcher:
    recording_started: Any
    recording_state_changed: Any
    recording_stopped: Any
    start_record_clicked: Any
    stop_record_clicked: Any

class StorageDispatcher:
    add_to_favourites_clicked: Any
    blacklist_song_clicked: Any
    manage_blacklist_clicked: Any
    manage_favourites_clicked: Any
