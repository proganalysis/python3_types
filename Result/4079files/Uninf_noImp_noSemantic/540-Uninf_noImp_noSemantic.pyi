from ika.service import Listener
from typing import Any

class Welcome(Listener):
    async def uid(self, sid: Any, uid: Any, timestamp: Any, nick: Any, host: Any, dhost: Any, ident: Any, ipaddress: Any, signon: Any, *modes_n_gecos: Any) -> None: ...
