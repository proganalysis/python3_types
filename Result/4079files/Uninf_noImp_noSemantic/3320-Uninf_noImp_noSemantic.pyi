import xml.etree.ElementTree as ET
import pathlib
import subprocess
import typing as t
from typing import Any

_LOG: Any

def execute_parser(input_path: pathlib.Path, output_path: t.Optional[pathlib.Path], verbosity: int=..., tokenize_instead: bool=..., *args: Any) -> subprocess.CompletedProcess: ...
def parse(input_path: pathlib.Path, verbosity: int=..., raise_on_error: bool=...) -> ET.Element: ...
