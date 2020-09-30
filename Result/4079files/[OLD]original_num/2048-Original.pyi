# (generated with --quick)

from typing import Any

CONFIG_FILE: str
CONFIG_KEY_AUTH: str
CONFIG_KEY_CERT: str
CONFIG_KEY_IP: str
CONFIG_KEY_LOCAL: str
CONFIG_KEY_PASSHASH: str
CONFIG_KEY_PORT: str
CONFIG_KEY_SSL: str
CONFIG_KEY_TOKEN: str
CONFIG_SECTION_INJ: str
CONFIG_SECTION_WEB: str
ServerHandler: Any
argparse: module
args: argparse.Namespace
config: configparser.ConfigParser
configparser: module
default_cert: str
default_ip: str
default_port: Any
default_usessl: bool
help_text: str
http: module
parser: argparse.ArgumentParser
ssl: module
web: configparser.SectionProxy

def python_version() -> str: ...
def run_https_server(cert = ..., ip = ..., port = ..., usessl = ...) -> None: ...
