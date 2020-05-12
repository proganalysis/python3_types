from typing import Any

def normalize_network(network: Any): ...

class DefaultConfiguration:
    rtn_msg_interval: int = ...
    rtn_msg_interval_jitter: Any = ...
    rtn_msg_hold_time: Any = ...
    retracted_prefix_hold_time: Any = ...
    max_full_update_interval: int = ...
    enable_full_only_mode: bool = ...
    DEFAULT_CONFIG: Any = ...
    LINK_CHARACTERISTICS_BANDWIDTH: int = ...
    LINK_CHARACTERISTICS_LOSS: int = ...
    LINK_CHARACTERISTICS_COST: int = ...
    DEFAULT_ATTRIBUTES: Any = ...
    @staticmethod
    def validate_config(configuration: dict) -> dict: ...
