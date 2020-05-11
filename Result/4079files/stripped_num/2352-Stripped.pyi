# (generated with --quick)

from typing import Dict, Optional

ENDIAN_BIG: int
ENDIAN_LITTLE: int
ENDIAN_UNKNOWN: int
FILE_FORMAT_AMIGA_HUNK_EXECUTABLE: int
FILE_FORMAT_AMIGA_HUNK_LIBRARY: int
FILE_FORMAT_ATARIST_GEMDOS_EXECUTABLE: int
FILE_FORMAT_SNES_SMC: int
FILE_FORMAT_UNKNOWN: int
FILE_FORMAT_X68000_X_EXECUTABLE: int
FILE_FORMAT_ZXSPECTRUM_Z80_1: int
FILE_FORMAT_ZXSPECTRUM_Z80_2: int
FILE_FORMAT_ZXSPECTRUM_Z80_3: int
MATCH_CERTAIN: int
MATCH_NONE: int
MATCH_POSSIBLE: int
MATCH_PROBABLE: int
PLATFORM_AMIGA: int
PLATFORM_ATARIST: int
PLATFORM_SNES: int
PLATFORM_UNKNOWN: int
PLATFORM_X68000: int
PLATFORM_ZXSPECTRUM: int
PROCESSOR_65c816: int
PROCESSOR_M68000: int
PROCESSOR_M68010: int
PROCESSOR_M68020: int
PROCESSOR_M68030: int
PROCESSOR_M68040: int
PROCESSOR_M68060: int
PROCESSOR_M680x0: int
PROCESSOR_MIPS: int
PROCESSOR_UNKNOWN: int
PROCESSOR_Z80: int
endian_names: Dict[int, str]
file_format_names: Dict[int, str]
platform_names: Dict[int, str]
processor_names: Dict[int, str]

class MatchResult(object):
    confidence: int
    file_format_id: int
    platform_id: int

def __import_data_types() -> None: ...
def lookup_processor_id_by_name(specified_processor_name) -> Optional[int]: ...
