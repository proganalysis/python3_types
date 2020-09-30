# (generated with --quick)

import qrays
from typing import Any, Type

A: qrays.Qvector
AtoZ: str
B: qrays.Qvector
C: qrays.Qvector
D: qrays.Qvector
E: qrays.Qvector
F: qrays.Qvector
G: qrays.Qvector
H: qrays.Qvector
I: qrays.Qvector
J: qrays.Qvector
K: qrays.Qvector
L: qrays.Qvector
M: qrays.Qvector
N: qrays.Qvector
O: qrays.Qvector
P: qrays.Qvector
Q: qrays.Qvector
Qvector: Type[qrays.Qvector]
R: qrays.Qvector
S: qrays.Qvector
T: qrays.Qvector
U: qrays.Qvector
V: qrays.Qvector
W: qrays.Qvector
X: qrays.Qvector
Y: qrays.Qvector
Z: qrays.Qvector
os: module
sql: module
sys: module
time: module

class DB:
    backend: str
    c: Any
    conn: Any
    db_name: str
    target_path: str
    timezone: int
    @classmethod
    def connect(cls) -> None: ...
    @classmethod
    def disconnect(cls) -> None: ...

def make_tables() -> None: ...
def save_coords() -> None: ...
def save_faces() -> None: ...
def save_polys() -> None: ...
