# (generated with --quick)

import random
from typing import Any, Type

ElementTree: module
NistBeaconCrypto: Any
Random: Type[random.Random]
binascii: module
hashlib: module
json: module

class NistBeaconValue(object):
    _KEY_FREQUENCY: str
    _KEY_OUTPUT_VALUE: str
    _KEY_PREVIOUS_OUTPUT_VALUE: str
    _KEY_SEED_VALUE: str
    _KEY_SIGNATURE_VALUE: str
    _KEY_STATUS_CODE: str
    _KEY_TIMESTAMP: str
    _KEY_VERSION: str
    __doc__: str
    _frequency: Any
    _json: str
    _output_value: Any
    _previous_output_value: Any
    _pseudo_random: random.Random
    _seed_value: Any
    _signature_value: Any
    _status_code: Any
    _timestamp: Any
    _valid_signature: Any
    _version: Any
    _xml: str
    _xml_template: str
    frequency: Any
    json: Any
    output_value: Any
    previous_output_value: Any
    pseudo_random: Any
    seed_value: Any
    signature_value: Any
    status_code: Any
    timestamp: Any
    valid_signature: Any
    version: Any
    xml: Any
    def __eq__(self, other) -> Any: ...
    def __init__(self, version, frequency, timestamp, seed_value, previous_output_value, signature_value, output_value, status_code) -> None: ...
    @classmethod
    def from_json(cls, input_json) -> Any: ...
    @classmethod
    def from_xml(cls, input_xml) -> Any: ...
