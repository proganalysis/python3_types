from abc import ABC, abstractmethod
from scr.logic.circuit import Circuit
from typing import Dict

class PostSolver(ABC):
    @staticmethod
    def build(postsolver_name: str) -> PostSolver: ...
    @abstractmethod
    def post_solve(self, circuit: Circuit) -> Dict: ...
