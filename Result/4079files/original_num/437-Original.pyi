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
    _frequency: int
    _json: str
    _output_value: str
    _previous_output_value: str
    _pseudo_random: random.Random
    _seed_value: str
    _signature_value: str
    _status_code: str
    _timestamp: int
    _valid_signature: Any
    _version: str
    _xml: str
    _xml_template: str
    frequency: int
    json: str
    output_value: str
    previous_output_value: str
    pseudo_random: random.Random
    seed_value: str
    signature_value: str
    status_code: str
    timestamp: int
    valid_signature: bool
    version: str
    xml: str
    def __init__(self, version: str, frequency: int, timestamp: int, seed_value: str, previous_output_value: str, signature_value: str, output_value: str, status_code: str) -> None: ...
    @classmethod
    def from_json(cls, input_json: str) -> NistBeaconValue: ...
    @classmethod
    def from_xml(cls, input_xml: str) -> NistBeaconValue: ...
