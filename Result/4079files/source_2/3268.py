# Standard Library
import os
import shutil
from os import makedirs, mknod
from os.path import abspath, dirname, exists, isdir, isfile, realpath
# import types for static typing (mypy, pycharm etc)
from typing import Iterable, Optional, Text


def up_by_n_dirs(path: Text, n: int) -> Text:
    return path if n == 0 else up_by_n_dirs(dirname(path), n - 1)


def vimdir_path(*components) -> Text:
    return os.path.join(up_by_n_dirs(abspath(__file__), 4), *components)


def require_exists(fpath: Text) -> None:
    assert fpath, f"invalid path {fpath}"
    assert len(fpath) > 0, f"0-len path {fpath}"
    assert exists(fpath), f"non-existent path {fpath}"


def ensure_exists(fpath: Text) -> None:
    parent = dirname(fpath)
    if not isdir(parent):
        makedirs(parent)
    if not isfile(fpath):
        mknod(fpath)


def validate_executables(xs: Iterable[Text]) -> None:
    # verify that all necessary EXECUTABLES are present
    for exe in xs:
        path: Optional[Text] = shutil.which(exe)
        if path is not None and (type(path) == str):
            path = realpath(path)
        assert path is not None and os.path.exists(
            path
        ), f"one of the required executables \
                    '{exe if not path else path}' not installed"
