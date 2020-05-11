# (generated with --quick)

from typing import Any, Dict, Generator, List, TypeVar, Union

_T0 = TypeVar('_T0')
_TCaptionableMessage = TypeVar('_TCaptionableMessage', bound=CaptionableMessage)
_TMessage = TypeVar('_TMessage', bound=Message)
_TOutApiObject = TypeVar('_TOutApiObject', bound=OutApiObject)

class ApiObject:
    _type: Any
    data: Any
    def __getattr__(self, item) -> Any: ...
    def __init__(self, _type = ..., **data) -> None: ...
    def get_or_default(self, key, default = ...) -> Any: ...
    def get_or_fail(self, key) -> Any: ...
    def get_type(self) -> Any: ...
    def unwrap_api_object(self) -> Dict[str, Any]: ...
    @staticmethod
    def wrap_api_object(data: _T0) -> Union[ApiObject, ApiObjectList, _T0]: ...

class ApiObjectList:
    data_list: list
    def _ApiObjectList__wrapped_api_objects(self) -> Generator[Any, Any, None]: ...
    def __init__(self, data_list: list) -> None: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def unwrap_api_object(self) -> list: ...

class Audio(CaptionableMessage):
    _type: Any
    data: Dict[str, Any]
    @staticmethod
    def create_audio(file_id) -> Audio: ...

class CaptionableMessage(Message):
    _type: Any
    data: Dict[str, Any]
    def with_caption(self: _TCaptionableMessage, caption_text) -> _TCaptionableMessage: ...

class Contact(Message):
    _type: Any
    data: Dict[str, Any]
    @staticmethod
    def create_contact(phone_number, first_name, last_name = ...) -> Contact: ...

class Document(CaptionableMessage):
    _type: Any
    data: Dict[str, Any]
    @staticmethod
    def create_document(file_id) -> Document: ...

class Location(Message):
    _type: Any
    data: Dict[str, Any]
    @staticmethod
    def create_location(latitude, longitude) -> Location: ...

class Message(OutApiObject):
    _type: Any
    data: Dict[str, Any]
    def copy(self: _TMessage) -> _TMessage: ...
    @staticmethod
    def create(text, chat_id = ..., **kwargs) -> Message: ...
    @staticmethod
    def create_reply(message, reply_text) -> Message: ...
    def inline_message_id(self: _TMessage, inline_message_id: int) -> _TMessage: ...
    def reply_to_message(self: _TMessage, message = ..., message_id = ...) -> _TMessage: ...
    def set_message_id(self, message_id) -> None: ...
    def to_chat(self: _TMessage, chat = ..., message = ..., chat_id = ...) -> _TMessage: ...
    def to_chat_replying(self: _TMessage, message) -> _TMessage: ...
    def with_reply_markup(self: _TMessage, reply_markup: dict) -> _TMessage: ...

class MessageEntityParser:
    text_as_utf16_bytes: Any
    def __init__(self, message) -> None: ...
    def get_entity_text(self, entity) -> Any: ...
    def get_text_after_entity(self, entity) -> Any: ...

class OutApiObject(ApiObject):
    LOCAL_PARAMS: List[str]
    LOCAL_PARAM_ERROR_CALLBACK: str
    LOCAL_PARAM_SCHEDULER: str
    _type: Any
    data: Dict[str, Any]
    def with_error_callback(self: _TOutApiObject, func) -> _TOutApiObject: ...

class Photo(CaptionableMessage):
    _type: Any
    data: Dict[str, Any]
    @staticmethod
    def create_photo(file_id) -> Photo: ...

class Sticker(Message):
    _type: Any
    data: Dict[str, Any]
    @staticmethod
    def create_sticker(file_id) -> Sticker: ...

class Video(CaptionableMessage):
    _type: Any
    data: Dict[str, Any]
    @staticmethod
    def create_video(file_id) -> Video: ...

class VideoNote(Message):
    _type: Any
    data: Dict[str, Any]
    @staticmethod
    def create_video_note(file_id, length) -> VideoNote: ...

class Voice(CaptionableMessage):
    _type: Any
    data: Dict[str, Any]
    @staticmethod
    def create_voice(file_id) -> Voice: ...
