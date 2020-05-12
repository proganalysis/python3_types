from cryptography.hazmat.primitives.asymmetric import rsa as rsa
from typing import Any

__author__: str
keyserver: str

def serialize_signature(signature: bytes) -> str: ...
def ssh_public_key(keypair: rsa.RSAPrivateKeyWithSerialization) -> str: ...

class SSHManager:
    _key: Any = ...
    path: Any = ...
    logger: Any = ...
    token_path: Any = ...
    priv_path: Any = ...
    pub_path: Any = ...
    known_hosts_path: Any = ...
    authorized_keys_path: Any = ...
    def __init__(self, path: str = ...) -> None: ...
    @property
    def paramiko_key(self): ...
    @property
    def ssh_key(self): ...
    ssh_agentKey: Any = ...
    @ssh_key.setter
    def ssh_key(self, value: Any) -> None: ...
    @property
    def public_ssh_key_string(self) -> str: ...
    def get_new_key_from_server(self, token: Any): ...
    def write_key_to_path(self) -> None: ...
    def sign_message_PKCS1v15(self, message: Any) -> bytes: ...
    def sign_message_PSS(self, message: Any) -> bytes: ...
    def sign_message_PSS_b64(self, message: Any) -> bytes: ...
    def sign_message(self, message: Any) -> str: ...
