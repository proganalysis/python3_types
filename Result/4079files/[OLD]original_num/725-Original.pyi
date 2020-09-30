# (generated with --quick)

import objetodojogo
from typing import Any, Type

ObjetoDoJogo: Type[objetodojogo.ObjetoDoJogo]
Posicao2D: Type[objetodojogo.Posicao2D]
naleatorios: module
pygame: Any
som: module

class Alienigena(objetodojogo.ObjetoDoJogo):
    alienigenas_vivos: int
    dano: int
    ix: Any
    iy: Any
    pos_script: int
    posical_final: Any
    qmov: int
    resistencia: int
    script_movimento: Any
    valor: int
    def __init__(self, nome, pos, imagem, tipo = ...) -> None: ...
    def move(self, direcao) -> None: ...
    def set_script(self, script) -> None: ...

def __getattr__(name) -> Any: ...
