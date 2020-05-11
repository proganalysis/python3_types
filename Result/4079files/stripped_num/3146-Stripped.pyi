# (generated with --quick)

from typing import Set, TypeVar, Union

__author__: str
codecs: module
configparser: module
dir_path: str
file_path: str
os: module
translations: configparser.ConfigParser

_T0 = TypeVar('_T0')

def translate(string: _T0, language) -> Union[str, _T0]: ...
def translate_all(string: _T0) -> Set[Union[str, _T0]]: ...
