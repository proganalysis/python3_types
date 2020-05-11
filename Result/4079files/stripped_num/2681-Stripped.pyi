# (generated with --quick)

from typing import Any

ConfigurationException: Any
copy: module
functools: module
ipaddress: module
normalize_network: functools._lru_cache_wrapper

class DefaultConfiguration(object):
    DEFAULT_ATTRIBUTES: dict
    DEFAULT_CONFIG: dict
    LINK_CHARACTERISTICS_BANDWIDTH: int
    LINK_CHARACTERISTICS_COST: int
    LINK_CHARACTERISTICS_LOSS: int
    enable_full_only_mode: bool
    max_full_update_interval: int
    retracted_prefix_hold_time: int
    rtn_msg_hold_time: int
    rtn_msg_interval: int
    rtn_msg_interval_jitter: float
    @staticmethod
    def validate_config(configuration) -> Any: ...
