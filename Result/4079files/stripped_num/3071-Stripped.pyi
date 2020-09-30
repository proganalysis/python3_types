# (generated with --quick)

from typing import Any

configparser: module

class Config:
    Download: Any
    Download_Docs: Any
    Download_Method: Any
    Download_Path: Any
    Download_Queue_Length: int
    Download_Srt: Any
    cookies: Any
    login_method: Any
    password: Any
    username: Any
    def __init__(self, setting) -> None: ...

def load_config(config_file, site) -> Config: ...
def str2bool(v) -> bool: ...
