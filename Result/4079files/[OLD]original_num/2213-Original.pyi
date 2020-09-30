# (generated with --quick)

import __future__
import cryptography.exceptions
from typing import Any, NoReturn, Type

UnsupportedAlgorithm: Type[cryptography.exceptions.UnsupportedAlgorithm]
_DHParameters: Any
_DHPrivateKey: Any
_DHPublicKey: Any
_Reasons: Any
absolute_import: __future__._Feature
dh: module
division: __future__._Feature
print_function: __future__._Feature
serialization: module
utils: Any

def _dh_cdata_to_parameters(dh_cdata, backend) -> Any: ...
def _dh_params_dup(dh_cdata, backend) -> Any: ...
def _get_dh_num_bits(backend, dh_cdata) -> Any: ...
def _handle_dh_compute_key_error(errors, backend) -> NoReturn: ...
