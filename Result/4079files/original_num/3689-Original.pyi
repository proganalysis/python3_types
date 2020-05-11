# (generated with --quick)

import cryptography.hazmat.primitives.asymmetric.rsa
from typing import Any

SysUtil: Any
__author__: str
hashes: module
io: module
keyserver: str
logging: module
os: module
padding: module
paramiko: Any
request: module
rsa: module
serialization: module
ssl: module
struct: module
textwrap: module
utils: Any

class SSHManager(object):
    __doc__: str
    _key: None
    authorized_keys_path: str
    known_hosts_path: str
    logger: logging.Logger
    paramiko_key: Any
    path: Any
    priv_path: str
    pub_path: str
    public_ssh_key_string: str
    ssh_agentKey: None
    ssh_key: Any
    token_path: str
    def __init__(self, path = ...) -> None: ...
    def get_new_key_from_server(self, token) -> bool: ...
    def sign_message(self, message) -> str: ...
    def sign_message_PKCS1v15(self, message) -> bytes: ...
    def sign_message_PSS(self, message) -> bytes: ...
    def sign_message_PSS_b64(self, message) -> bytes: ...
    def write_key_to_path(self) -> None: ...

def b64encode(s: bytes, altchars: bytes = ...) -> bytes: ...
def default_backend() -> Any: ...
def serialize_signature(signature: bytes) -> str: ...
def ssh_public_key(keypair: cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKeyWithSerialization) -> str: ...
