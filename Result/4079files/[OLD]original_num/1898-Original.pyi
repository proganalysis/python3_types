# (generated with --quick)

configparser: module

class CmdParser(object):
    __doc__: str

class ConfigError(Exception):
    __doc__: str

class ConfigSettings(object):
    __doc__: str
    configure: configparser.ConfigParser
    ini_file: str
    def __init__(self, ini_file) -> None: ...
    def load_init(self) -> None: ...

class LazySettings(object): ...
