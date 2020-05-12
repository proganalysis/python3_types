from typing import Any

ELECTRUM_VERSION: str
APK_VERSION: str
PROTOCOL_VERSION: str
SEED_PREFIX: str
SEED_PREFIX_2FA: str
SEED_PREFIX_SW: str

def seed_prefix(seed_type: Any): ...
