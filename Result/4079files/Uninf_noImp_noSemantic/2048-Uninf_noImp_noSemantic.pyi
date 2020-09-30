CONFIG_FILE: str
CONFIG_SECTION_WEB: str
CONFIG_SECTION_INJ: str
CONFIG_KEY_IP: str
CONFIG_KEY_PORT: str
CONFIG_KEY_LOCAL: str
CONFIG_KEY_CERT: str
CONFIG_KEY_SSL: str
CONFIG_KEY_AUTH: str
CONFIG_KEY_PASSHASH: str
CONFIG_KEY_TOKEN: str

def run_https_server(cert: str = ..., ip: str = ..., port: int = ..., usessl: bool = ...) -> None: ...
