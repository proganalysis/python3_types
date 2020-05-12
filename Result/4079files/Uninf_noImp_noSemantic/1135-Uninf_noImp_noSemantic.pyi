from typing import Any

REFERENCE_DATE: Any
GROUP_ID_SIZE: int
SIGNATURE_SIZE: int
DIGESTMOD: Any
BASE64ENC: Any
__all__: Any

def generate_date_fragment(expiration_date: Any): ...
def generate_msg_part_for_group(group: Any, expiration_date: Any): ...
def sign_code(msg: Any): ...
def generate_code_for_group(group: Any, expiration_date: Any): ...
def get_next_promo_code(group: Any): ...
def is_promo_code_delayed(): ...
def next_promo_code_date(): ...
