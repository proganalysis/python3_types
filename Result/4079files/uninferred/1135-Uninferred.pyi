import base64
import hashlib
from typing import Any

DIGESTMOD = hashlib.sha1
BASE64ENC = base64.urlsafe_b64encode

def get_next_promo_code(group: Any): ...
