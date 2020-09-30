# (generated with --quick)

enum: module

class AuthType(enum.IntEnum):
    RSAPUBLICKEY: int
    SIGNATURE: int
    TOKEN: int
    __doc__: str

class Command(enum.IntEnum):
    AUTH: int
    CLSE: int
    CNXN: int
    OKAY: int
    OPEN: int
    SYNC: int
    WRTE: int
    __doc__: str

class CommandResponse(enum.Enum):
    FAIL: str
    OKAY: str
    __doc__: str

class SystemType(enum.Enum):
    BOOTLOADER: str
    DEVICE: str
    HOST: str
    __doc__: str
