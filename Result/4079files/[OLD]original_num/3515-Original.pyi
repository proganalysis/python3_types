# (generated with --quick)

import asyncio.events
from typing import Any, Pattern

BLACKLIST: Any
Slacker: Any
USER_TOKEN: Any
asyncio: module
bot: Any
client: Any
concurrent: module
loop: asyncio.events.AbstractEventLoop
re: module
re_chan: Pattern[str]
re_link: Pattern[str]
re_user: Pattern[str]

def get_all_channels() -> Any: ...
def get_all_users() -> Any: ...
def get_user_message_history(user_name, channels) -> Any: ...
def get_user_name_by_id(user_id) -> Any: ...
def sanitize_chan_str(txt, match) -> str: ...
def sanitize_link_str(txt, match) -> str: ...
def sanitize_slack_str(text) -> Any: ...
def sanitize_user_str(txt, match) -> Any: ...
def send_user_dm(u_id, text) -> Any: ...
