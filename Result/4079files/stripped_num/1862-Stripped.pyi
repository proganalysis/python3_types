# (generated with --quick)

import concurrent.futures.process
from typing import Any, Type

BICO: Any
KMeans: Any
Point: Any
X_chunks: Any
X_varied: Any
concurrent: module
datetime: Type[datetime.datetime]
executor: concurrent.futures.process.ProcessPoolExecutor
logging: module
make_blobs: Any
multiprocessing: module
n_samples: int
np: module
os: module
proj_method: str
projections: int
random_state: int
tend: datetime.datetime
tstart: datetime.datetime
y_pred: Any
y_varied: Any

def run_bico(size, X) -> None: ...
def run_bico_parellel(X) -> None: ...
