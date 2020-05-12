# (generated with --quick)

import argparse
import configparser
from typing import Any, Dict, Type

ArgumentParser: Type[argparse.ArgumentParser]
ConfigParser: Type[configparser.ConfigParser]
Messaging: Any
logging: module
pluginmanager: Any
sys: module

def _get_command_line_args() -> Dict[str, Any]: ...
def _get_settings(settings_filepath) -> Dict[str, Dict[str, str]]: ...
def main(context = ..., *args, **kwargs) -> None: ...
