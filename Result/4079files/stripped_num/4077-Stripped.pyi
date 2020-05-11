# (generated with --quick)

import array
import mmap
from typing import Any, Callable, Dict, Tuple, TypeVar, Union

HAP_param_code_to_converter: Dict[int, Any]
HAP_param_name_to_converter: Dict[str, Any]
HAP_param_type_code_to_name: Dict[int, str]
HAP_param_type_name_to_code: Dict[str, int]
characteristic_ID_descriptor_UUID: str
format_code_to_name: Dict[int, str]
format_name_to_converter: Dict[str, Callable[[Any], Any]]
op_code_to_name: Dict[int, str]
pair_setup_characteristic_UUID: str
pair_verify_characteristic_UUID: str
pairing_features_characteristic_UUID: str
pairing_ktlv_error_code_to_name: Dict[int, str]
pairing_ktlv_method_value_code_to_name: Dict[int, str]
pairing_service_UUID: str
pairing_tlv_name_to_format: Dict[str, str]
pairing_tlv_value_to_name: Dict[int, str]
status_code_to_message: Dict[int, str]
status_code_to_name: Dict[int, str]
unit_code_to_name: Dict[int, str]
unit_name_to_code: Dict[str, int]

_T0 = TypeVar('_T0')

class HapBleOpCodes:
    Characteristic_Execute_Write: int
    Characteristic_Read: int
    Characteristic_Signature_Read: int
    Characteristic_Timed_Write: int
    Characteristic_Write: int
    Service_Signature_Read: int
    __doc__: str
    def __call__(self, code) -> str: ...

class HapBleStatusCodes:
    Insufficient_Authentication: int
    Insufficient_Authorization: int
    Invalid_Instance_ID: int
    Invalid_Request: int
    Max_Procedures: int
    Success: int
    Unsupported_PDU: int
    __doc__: str
    def __call__(self, code) -> str: ...

class HapParamTypes:
    Additional_Authorization_Data: int
    Characteristic_Instance_ID: int
    Characteristic_Type: int
    GATT_Presentation_Format_Descriptor: int
    GATT_User_Description_Descriptor: int
    GATT_Valid_Range: int
    HAP_Characteristic_Properties_Descriptor: int
    HAP_Linked_Services: int
    HAP_Service_Properties: int
    HAP_Step_Value_Descriptor: int
    HAP_Valid_Values_Descriptor: int
    HAP_Valid_Values_Range_Descriptor: int
    Origin_local_vs_remote: int
    Return_Response: int
    Service_Instance_ID: int
    Service_Type: int
    TTL: int
    Value: int
    def __call__(self, code) -> str: ...

class PairingKTLVErrorCodes:
    kTLVError_Authenticatio: int
    kTLVError_Backof: int
    kTLVError_Bus: int
    kTLVError_MaxPeer: int
    kTLVError_MaxTrie: int
    kTLVError_Unavailabl: int
    kTLVError_Unknow: int
    def __call__(self, code) -> str: ...

class PairingKTLVMethodValues:
    Add_Pairing: int
    List_Pairings: int
    Pair_Setup: int
    Pair_Verify: int
    Remove_Pairing: int
    Reserved: int
    __doc__: str
    def __call__(self, code) -> str: ...

class PairingKTlvValues:
    __doc__: str
    kTLVType_Certificate: int
    kTLVType_EncryptedData: int
    kTLVType_Error: int
    kTLVType_FragmentData: int
    kTLVType_FragmentLast: int
    kTLVType_Identifier: int
    kTLVType_Method: int
    kTLVType_Permissions: int
    kTLVType_Proof: int
    kTLVType_PublicKey: int
    kTLVType_RetryDelay: int
    kTLVType_Salt: int
    kTLVType_Separator: int
    kTLVType_Signature: int
    kTLVType_State: int
    def __call__(self, code) -> str: ...

def identity(x: _T0) -> _T0: ...
def parse_format(b) -> Tuple[Any, Any]: ...
def to_bool(b) -> Any: ...
def to_float(b) -> Any: ...
def to_int32(b) -> Any: ...
def to_uint16(b) -> Any: ...
def to_uint32(b) -> Any: ...
def to_uint64(b) -> Any: ...
def to_uint8(b) -> Any: ...
def to_utf8(b) -> Any: ...
def to_uuid(b) -> str: ...
def unpack(fmt: Union[bytes, str], buffer: Union[bytearray, bytes, memoryview, mmap.mmap, array.array[int]]) -> tuple: ...
