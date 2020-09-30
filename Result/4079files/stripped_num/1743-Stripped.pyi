# (generated with --quick)

import datetime
import json.encoder
from typing import Any, List, Optional, Type

JSONEncoder: Type[json.encoder.JSONEncoder]
date: Type[datetime.date]
json: module
re: module

class Bloco(object):
    descricao: Any
    nome: Any
    def __init__(self, nome, descricao) -> None: ...

class Campo(object):
    decimal: Optional[int]
    descricao: Any
    indice: Optional[int]
    nome: Any
    obrigatorio: Any
    regras: Any
    tamanho: Optional[int]
    tipo: Any
    valores: Any
    def __init__(self, indice, nome, descricao, tipo, tamanho, decimal, valores, obrigatorio, regras) -> None: ...

class Leiaute(object):
    blocos: Any
    data_inicio: Any
    registros: Any
    tipo: Any
    versao: Any
    def __init__(self, tipo, versao, data_inicio, blocos, registros) -> None: ...

class LeiauteEncoder(json.encoder.JSONEncoder): ...

class Registro(object):
    campos: List[nothing]
    campos_chave: Any
    codigo: Any
    nivel: Any
    nome: Any
    ocorrencia: Any
    regras: Any
    def __init__(self, codigo, nome, regras, nivel, ocorrencia, campos_chave) -> None: ...

def extrair_parametros(s) -> list: ...
def normalize_quotes(s) -> Any: ...
def normalize_spaces(s) -> str: ...
def remove_space(s) -> str: ...
