from typing import Any

orig_build_class = __build_class__

class A: ...

def custom_import(name: Any, globals: Any, locals: Any, fromlist: Any, level: Any): ...
