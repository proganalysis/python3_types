from typing import Any

instruction_file: str
args_file: str
output_functions: str
output_binding: str
arg_regex: str
d: Any
functions_file: Any
binding_file: Any
function_template: str
binding_template: str
type_names: Any
var_names: Any

def arg_type(x: Any, el: Any): ...
def impl_sig(opcode: Any, sig: Any): ...
def adjust_args(args: Any): ...

coordinates: Any
colours: Any

def check_vector(typeName: Any, argName: Any, doc: Any, args: Any, x: Any) -> None: ...
def check_colour(typeName: Any, argName: Any, doc: Any, args: Any, x: Any) -> None: ...
def process_args(args: Any): ...
def finalize_args(args: Any): ...

m: Any
opcode: Any
argc: Any
func: Any
am: Any
sig: Any
xpath: Any
res: Any
args: Any
sa_name: Any
eargs: Any
postfix: str
signame: Any
argsdoc: str
parameters: Any
