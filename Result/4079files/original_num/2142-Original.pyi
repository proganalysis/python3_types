# (generated with --quick)

import pathlib
from typing import Any, Type

BooleanField: Any
CharField: Any
DateTimeField: Any
DoesNotExist: Any
DopplerrDb: Any
ForeignKeyField: Any
IntegerField: Any
Model: Any
Path: Type[pathlib.Path]
PrimaryKeyField: Any
SqliteQueueDatabase: Any
TextField: Any
Using: Any
datetime: module
singleton: Any

class Events(Any):
    message: Any
    timestamp: Any
    type: Any

class SeriesMedias(Any):
    added_timestamp: Any
    dirty: Any
    episode_number: Any
    episode_title: Any
    id: Any
    media_filename: Any
    quality: Any
    season_number: Any
    series_title: Any
    tv_db_id: Any
    video_languages: Any

class SeriesSubtitles(Any):
    added_timestamp: Any
    language: Any
    series_media: Any
