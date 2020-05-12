# (generated with --quick)

import argparse
import configparser
from typing import Any, Type

ArgumentParser: Type[argparse.ArgumentParser]
ConfigParser: Type[configparser.ConfigParser]
Messaging: Any
logging: module
pluginmanager: Any
sys: module

def _get_command_line_args() -> dict: ...
def _get_settings(settings_filepath) -> dict: ...
def main(context = ..., *args, **kwargs) -> None: ...
