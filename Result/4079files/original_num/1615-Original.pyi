# (generated with --quick)

from typing import Any

IF_Z80: int
instruction_table: list
logger: logging.Logger
logging: module

class ArchZ80(Any):
    constant_binary_prefix: str
    constant_binary_suffix: str
    constant_comment_prefix: str
    constant_core_architecture_mask: int
    constant_decimal_prefix: str
    constant_decimal_suffix: str
    constant_endian_types: str
    constant_hexadecimal_prefix: str
    constant_hexadecimal_suffix: str
    constant_immediate_prefix: str
    constant_pc_offset: int
    constant_register_prefix: str
    constant_word_size: int

def __getattr__(name) -> Any: ...
def _extend_instruction_table() -> None: ...
