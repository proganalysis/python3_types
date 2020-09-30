# (generated with --quick)

import multiprocessing.queues
from typing import Callable, Tuple

APPLICATION_NAME: str
argparse: module
logging: module
multiprocessing: module
os: module
sys: module
threading: module

def get_arguments() -> argparse.Namespace: ...
def get_configured_logger(user_folder, is_debug) -> Tuple[logging.Logger, multiprocessing.queues.Queue[nothing], logging.Formatter, int, Callable]: ...
def main() -> None: ...
