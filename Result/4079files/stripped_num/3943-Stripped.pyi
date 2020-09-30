# (generated with --quick)

import itertools
import modules.apis.kraken
import modules.apis.newbs
import modules.apis.osu
import modules.apis.splits_io
import modules.apis.sr_com
import modules.apis.srl
import modules.apis.youtube
from typing import Any, Dict, Type, Union

GLOBAL_APIS: Dict[str, Union[modules.apis.kraken.Kraken, modules.apis.newbs.NewbsAPI, modules.apis.osu.OsuAPI, modules.apis.splits_io.SplitsIOAPI, modules.apis.sr_com.SRcomAPI, modules.apis.srl.SRLAPI, modules.apis.youtube.YoutubeAPI]]
NewBotException: Any
RUNNING: bool
balancer: module
chain: Type[itertools.chain]
configuration: module
kraken: module
logging: module
newbs: module
os: module
osu: module
saltybot: module
setup_env: module
splits_io: module
sr_com: module
srl: module
threading: module
time: module
youtube: module

def listen_thread(config_obj, balancer_obj, server_obj) -> None: ...
def main() -> None: ...
def twitch_update_thread(balancer_obj) -> None: ...
