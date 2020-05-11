# (generated with --quick)

import subprocess
from typing import Any, Type

CalledProcessError: Type[subprocess.CalledProcessError]
KAFKA_HOST: Any
KAFKA_PATH: Any
KafkaConsumer: Any
KafkaProducer: Any
PIPE: int
Popen: Type[subprocess.Popen]
TIME_FORMAT_DAY: Any
TIME_FORMAT_SEC: Any
ZK_KAFKA_HOST: Any
datetime: module
fetch_ticks: Any
get_kafka_kdata_topic: Any
get_kafka_tick_topic: Any
get_kdata: Any
get_security_list: Any
get_ticks: Any
json: module
logger: logging.Logger
logging: module
producer: Any
to_security_item: Any

def _kdata_to_kafka(security_item, fuquan = ...) -> None: ...
def _tick_to_kafka(security_item) -> None: ...
def cryptocurrency_tick_to_kafka(exchange, pairs = ...) -> None: ...
def delete_all_topics() -> None: ...
def delete_topic(topic) -> None: ...
def kdata_to_kafka(security_item = ..., fuquan = ...) -> None: ...
def list_topics() -> Any: ...
def tick_to_kafka(security_item = ...) -> None: ...
