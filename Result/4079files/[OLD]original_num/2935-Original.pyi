# (generated with --quick)

import requests.exceptions
from typing import Any, Optional, Tuple, Type

ATTACHMENT: Any
BaseBotInstance: Any
BasePhotoStore: Any
CARD: Any
ChannelType: Any
EmptyBot: Any
FRIENDS: Any
Imgur: Any
MAP: Any
Message: Any
MessageBus: Any
MessageType: Any
MissingSchema: Type[requests.exceptions.MissingSchema]
MsgDirection: Any
NOTE: Any
PICTURE: Any
RECORDING: Any
SHARING: Any
SYSTEM: Any
TEXT: Any
VIDEO: Any
VOICE: Any
VimCN: Any
argparse: module
args: argparse.Namespace
config: Any
get_logger: Any
get_now_date_time: Any
get_qiniu: Any
get_redis: Any
imghdr: module
io: module
itchat: Any
logger: Any
myUid: Any
on_attachment_message: Any
on_card_message: Any
on_map_message: Any
on_note_message: Any
on_picture_message: Any
on_recording_message: Any
on_sharing_message: Any
on_text_message: Any
on_video_message: Any
on_voice_message: Any
parser: argparse.ArgumentParser
photo_store: Any
sys: module
wxHandle: Optional[WechatHandle]
wxRoomNicks: dict
wxRooms: dict

class WechatHandle(Any):
    ChanTag: Any
    SupportMultiline: bool
    SupportPhoto: bool
    send_to_bus: Any
    def __init__(self, roomNicks) -> None: ...
    def send_msg(self, target, content, sender = ..., first = ..., **kwargs) -> None: ...
    def send_photo(self, target, photo_data, sender = ...) -> None: ...

def Fishroom2WechatThread(wx: WechatHandle, bus) -> None: ...
def Wechat2FishroomThread(wx: WechatHandle, bus) -> None: ...
def handle_message(msg, content) -> None: ...
def init() -> Tuple[WechatHandle, Any, Any]: ...
def log_message(msgtype, msg) -> None: ...
def main() -> None: ...
def test() -> None: ...
def upload_photo(data) -> Tuple[Any, Optional[str]]: ...
def wechatExit() -> None: ...
def wxdebug() -> None: ...
