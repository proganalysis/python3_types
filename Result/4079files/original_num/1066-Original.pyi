# (generated with --quick)

import objetodojogo
from typing import Any, Type

ObjetoDoJogo: Type[objetodojogo.ObjetoDoJogo]
Posicao2D: Type[objetodojogo.Posicao2D]
clock: Any
pygame: Any
traducao: module

class Score(objetodojogo.ObjetoDoJogo):
    __doc__: str
    fonte: Any
    imagem: Any
    jogador: None
    def __init__(self, nome, pos = ...) -> None: ...

class ScoreComFPS(Score):
    fonte: Any
    imagem: Any
    jogador: None
    def __init__(self, nome, pos) -> None: ...

class Texto(objetodojogo.ObjetoDoJogo):
    __doc__: str
    cor: Any
    fonte: Any
    imagem: Any
    jogador: None
    pos: list
    resistencia: Any
    texto: Any
    universo: Any
    def __init__(self, nome, pos, texto, tamanho, tempo, universo, cor) -> None: ...

def __getattr__(name) -> Any: ...
