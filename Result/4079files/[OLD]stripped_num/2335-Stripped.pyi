
from typing import Any
def __getattr__(name: Any) -> Any: ...
# Caught error in pytype: 'logging.StreamHandler'
# Traceback (most recent call last):
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 156, in check_or_generate_pyi
#     input_filename=options.input, options=options, loader=loader)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 113, in generate_pyi
#     analyze.infer_types, input_filename, options, loader)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 65, in wrapper
#     return f(*args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 84, in _call
#     deep=deep)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 652, in infer_types
#     loc, defs = tracer.run_program(src, filename, init_maximum_depth)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 752, in run_program
#     node, f_globals, f_locals, _ = self.run_bytecode(node, code)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 720, in run_bytecode
#     node, return_var = self.run_frame(frame, node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 322, in run_frame
#     state = self.run_instruction(op, state)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 287, in run_instruction
#     state = bytecode_fn(state, op)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 2679, in byte_IMPORT_NAME
#     module = self.import_module(name, full_name, level)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 1375, in import_module
#     module = self._import_module(name, level)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 1419, in _import_module
#     ast = self.loader.import_name(name)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/load_pytd.py", line 426, in import_name
#     ast = self._import_name(module_name)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/load_pytd.py", line 502, in _import_name
#     file_ast, path = self._import_file(module_name, module_name.split("."))
#   File "/usr/local/lib/python3.6/dist-packages/pytype/load_pytd.py", line 569, in _import_file
#     file_ast, full_path = self._load_pyi(path, module_name)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/load_pytd.py", line 596, in _load_pyi
#     ast = self.load_file(filename=full_path, module_name=module_name)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/load_pytd.py", line 242, in load_file
#     return self._process_module(module_name, filename, ast)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/load_pytd.py", line 263, in _process_module
#     module.ast = self._resolve_external_and_local_types(module.ast)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/load_pytd.py", line 211, in _resolve_external_and_local_types
#     pyval = pyval.Visit(local_lookup)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 213, in Visit
#     return _Visit(self, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 241, in _Visit
#     return _VisitNode(node, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 325, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 292, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 325, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 343, in _VisitNode
#     new_node = visitor.Visit(new_node, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/pytd_visitors.py", line 184, in Visit
#     self, node, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/visitors.py", line 599, in VisitNamedType
#     return pytd.ToType(self.unit.Lookup(node.name), allow_constants=False)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/pytd.py", line 77, in Lookup
#     return self._name2item[name]
# KeyError: 'logging.StreamHandler'