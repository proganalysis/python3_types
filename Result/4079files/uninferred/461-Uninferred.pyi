from typing import Any

A: Any
B: Any
C: Any
D: Any
E: Any
F: Any
G: Any
H: Any
I: Any
J: Any
K: Any
L: Any
M: Any
N: Any
O: Any
P: Any
Q: Any
R: Any
S: Any
T: Any
U: Any
V: Any
W: Any
X: Any
Y: Any
Z: Any

class DB:
    backend: str = ...
    timezone: Any = ...
    target_path: Any = ...
    db_name: str = ...
    @classmethod
    def connect(cls) -> None: ...
    @classmethod
    def disconnect(cls) -> None: ...

def make_tables() -> None: ...
def save_polys() -> None: ...
def save_faces() -> None: ...
def save_coords() -> None: ...
