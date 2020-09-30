# (generated with --quick)

from typing import Dict, List, Tuple

DEFAULT_NUM_THREADS: int
GLOBAL_TIMEOUT: int
argparse: module
args: argparse.Namespace
cf: module
futures: module
parser: argparse.ArgumentParser
requests: module
source_names: str
sys: module
time: module
times: Dict[str, List[float]]

def fetch(iso_cc, source) -> Tuple[int, str]: ...
def main(source, num_threads) -> None: ...
