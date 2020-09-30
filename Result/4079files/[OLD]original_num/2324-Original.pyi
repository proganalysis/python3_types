# (generated with --quick)

import click.core
from typing import Any

Item: Any
JID: Any
Message: Any
MessageType: Any
Presence: Any
PresenceShow: Any
PresenceType: Any
State: Any
Template: Any
agent: Any
aioxmpp: Any
asyncio: module
behaviour: Any
click: module
datetime: module
random: module
run: click.core.Command
time: module

class WebAgent(Any):
    DummyBehav: type
    DummyFSMBehav: type
    DummyPeriodBehav: type
    DummyTimeoutBehav: type
    def add_fake_contact(self, jid, presence, show = ...) -> None: ...
    def setup(self) -> None: ...
