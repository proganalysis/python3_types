from collections import namedtuple
from typing import Any

TypeSpec = namedtuple('TypeSpec', 'pytype objctype o2p_code p2o_code')

ArgSpec = namedtuple('ArgSpec', 'argname typespec')

MethodSpec = namedtuple('MethodSpec', 'pyname objcname argspecs returntype is_inherited')

ClassSpec = namedtuple('ClassSpec', 'clsname superclass methodspecs is_protocol follow_protocols')
TYPE_SPECS: Any
PYTYPE2SPEC: Any
OBJCTYPE2SPEC: Any
DATA_PATH: Any

def tmpl_replace(tmpl: Any, **replacments: Any): ...
def get_objc_signature(methodspec: Any): ...
def copy_objp_unit(destfolder: Any) -> None: ...
