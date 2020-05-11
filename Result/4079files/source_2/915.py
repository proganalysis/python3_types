#! python3

import _io
import datetime
from typing import Iterable


def add_timestamp(entry: str) -> str:
    timestamp = str(tuple(datetime.datetime.now().timetuple())[:6])
    timestamp = '{0}{1} '.format(' ' * (25 - len(timestamp)), timestamp)
    entry = entry.replace('\n', '\n'+timestamp)
    return timestamp + entry


def remove_timestamp(entry: str) -> str:
    return entry[27:]


def get_timestamp(entry: str) -> str:
    return entry[:27].strip()


def write_with_timestamps(file: _io.TextIOWrapper, entries: Iterable[str]) -> None:
    for e in entries:
        file.write(add_timestamp(e))


def read_wo_timestamps(entries: Iterable[str]) -> Iterable[str]:
    return [remove_timestamp(e) for e in entries]


def timetuple(entry: str):
    time = datetime.datetime.strptime(get_timestamp(entry),  '(%Y, %m, %d, %H, %M, %S)')
    return entry, time
