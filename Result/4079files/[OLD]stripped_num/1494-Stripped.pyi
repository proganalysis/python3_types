# (generated with --quick)

from typing import Any, Callable, Dict, Iterable, Sized, Tuple, Type, TypeVar

ImageInformation = `namedtuple-ImageInformation-build_date-image_type`

collections: module
logging: module
os: module
socket: module
sys: module
yaml: module

_Tnamedtuple-ImageInformation-build_date-image_type = TypeVar('_Tnamedtuple-ImageInformation-build_date-image_type', bound=`namedtuple-ImageInformation-build_date-image_type`)

class Config:
    __doc__: str
    enrollment_uucp_dir: Any
    enrollment_uucp_path: Any
    hostname: Any
    image_information_file: Any
    ingest_uucp_dir: Any
    ingest_uucp_host: Any
    ingest_uucp_path: Any
    logger: logging.Logger
    ndr_netconfig_file: Any
    nmap_configuration_file: Any
    outgoing_enrollment_spool: Any
    outgoing_upload_spool: Any
    ssl_bundle: Any
    ssl_cafile: Any
    ssl_certfile: Any
    ssl_csr: Any
    ssl_private_key: Any
    tshark_ndr_binary: Any
    upload_method: Any
    def __init__(self, yaml_file) -> None: ...
    def get_image_version(self) -> `namedtuple-ImageInformation-build_date-image_type`: ...
    def to_dict(self) -> Dict[str, Any]: ...

class `namedtuple-ImageInformation-build_date-image_type`(tuple):
    __slots__ = ["build_date", "image_type"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    build_date: Any
    image_type: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-ImageInformation-build_date-image_type`], build_date, image_type) -> `_Tnamedtuple-ImageInformation-build_date-image_type`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-ImageInformation-build_date-image_type`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-ImageInformation-build_date-image_type`: ...
    def _replace(self: `_Tnamedtuple-ImageInformation-build_date-image_type`, **kwds) -> `_Tnamedtuple-ImageInformation-build_date-image_type`: ...
