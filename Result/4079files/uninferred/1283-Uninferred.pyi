import abc
from abc import ABC, abstractmethod
from scr.logic.circuit import Circuit as Circuit
from typing import Dict

class PostSolver(ABC, metaclass=abc.ABCMeta):
    @staticmethod
    def build(postsolver_name: str) -> PostSolver: ...
    @abstractmethod
    def post_solve(self, circuit: Circuit) -> Dict: ...
