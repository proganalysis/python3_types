from scipy.misc import imread as imread
from scipy.sparse import coo_matrix as coo_matrix
from time import time as time
from typing import Any

params: Any
f_rates: Any
folders: Any
backend: str
n_processes: Any
single_thread: bool
dview: Any
slurm_script: str
pdir: Any
profile: Any
c: Any
pars: Any
fls: Any

def processor_placeholder(pars: Any): ...

res: Any

def create_images_for_labeling(pars: Any): ...
