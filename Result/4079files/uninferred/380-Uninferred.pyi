from PyQt4 import QtCore as QtCore, QtGui as QtGui
from subprocess import call as call
from typing import Any

hostdir: Any
local: str
picsdir: Any

def run_program(rcmd: Any): ...
def scan_directories() -> None: ...
def create_html_head() -> None: ...
def create_html_output_dirs() -> None: ...
def create_html_output_rd_fail() -> None: ...
def create_html_output_pics(pdir: Any) -> None: ...
def upload() -> None: ...
def save_uploaded_file(tdir: Any): ...
def clean(newdir: Any, maxlen: Any): ...

form: Any
loc: str
f: Any
dummy: Any
success: Any
file: Any
