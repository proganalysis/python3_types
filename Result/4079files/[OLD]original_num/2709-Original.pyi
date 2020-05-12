# (generated with --quick)

from typing import Any, Type

Broker: Type[algobroker.Broker]
algobroker: module
bp: BrokerTwilio
my_path: Any
pprint: module
twilio: Any

class BrokerTwilio(algobroker.Broker):
    api: Any
    auth_id: Any
    auth_token: Any
    dst_number: Any
    src_number: Any
    def __init__(self) -> None: ...
    def process_control(self, data) -> None: ...
    def process_data(self, data) -> None: ...
