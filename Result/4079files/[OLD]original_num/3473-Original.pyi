# (generated with --quick)

from typing import Any, Type
import unittest.case
import unittest.mock

ListOfSpeakersViewSet: Any
MagicMock: Any
TestCase: Type[unittest.case.TestCase]
patch: unittest.mock._patcher

class ListOfSpeakersViewSetManageSpeaker(unittest.case.TestCase):
    __doc__: str
    mock_list_of_speakers: Any
    request: Any
    test_add_oneself_as_speaker: Any
    test_add_someone_else_as_speaker: Any
    test_remove_oneself: Any
    test_remove_someone_else: Any
    view_instance: Any

class ListOfSpeakersViewSetSpeak(unittest.case.TestCase):
    __doc__: str
    mock_list_of_speakers: Any
    request: Any
    test_begin_speech_specific_speaker: Any
    test_end_speech: Any
    view_instance: Any
    def test_begin_speech(self) -> None: ...
