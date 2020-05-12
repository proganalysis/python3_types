import os
from typing import Union

from pyow.casc import CASCManager, Record, DLLRecord
from pyow.dll_loader import load_dll
from pyow.owtypes.texture import OWTexture

load_dll()

# noinspection PyUnresolvedReferences
from System.IO import Stream, File, FileMode, FileAccess, MemoryStream
# noinspection PyUnresolvedReferences
from OWLib import ImageDefinition, STUD


class OWDecal(OWTexture):
    # noinspection PyMethodOverriding
    @classmethod
    def from_file(cls, file: str, man: CASCManager):
        if not os.path.exists(file):
            raise FileNotFoundError(file)
        stream = File.Open(file, FileMode.Open, FileAccess.Read)
        ret = cls._from_stream(stream, man)
        stream.Dispose()
        ret._file = file
        return ret

    @classmethod
    def from_record_with_data(cls, record: Union[Record, int], record_data: Union[Record, int], man: CASCManager):
        raise TypeError()

    @classmethod
    def from_record(cls, record: Union[Record, int], man: CASCManager):
        if isinstance(record, DLLRecord) or isinstance(record, int):
            record = man.map.get_record(record)
        if record is None:
            return
        record_stream = man.open_record(record)
        ret = cls._from_stream(record_stream, man)
        record_stream.Dispose()
        ret._record = record
        ret._casc_file = record.file
        return ret

    @classmethod
    def from_casc(cls, file: str, man: CASCManager):
        stream = man.get_file_stream(file)
        ret = cls._from_stream(stream, man)
        stream.Dispose()
        ret._casc_file = file
        return ret

    @classmethod
    def _from_stream(cls, stream: Stream, man: CASCManager):
        decal_stud = STUD(stream)
        if decal_stud.Instances is None:
            return
        decal = decal_stud.Instances[0]
        if decal is None:
            return
        with man.map.with_record(decal.Records[0].definiton) as rec:
            definition = ImageDefinition(man.open_record(rec))
            image_key = definition.Layers[0].key
            with man.map.with_record(image_key) as image_record:
                image_data_key = (image_key & 0xFFFFFFFF) | 0x100000000 | 0x0320000000000000
                return super(OWDecal, cls).from_record_with_data(image_record, image_data_key, man)

    @staticmethod
    def requires_04D(file_004: str, close: bool = True):
        raise TypeError()

    @staticmethod
    def get_04D_name(file_name: str, stream: Stream=None, close_stream: bool=True):
        raise TypeError()
