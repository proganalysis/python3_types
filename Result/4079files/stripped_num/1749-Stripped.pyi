
from typing import Any
def __getattr__(name: Any) -> Any: ...
# Caught error in pytype: 'set' object has no attribute 'extend'
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
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 2615, in byte_CALL_FUNCTION
#     return self.call_function_from_stack(state, op.arg, None, None)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 1077, in call_function_from_stack
#     state, func, posargs, namedargs, starargs, starstarargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 951, in call_function_with_state
#     starstarargs=starstarargs), fallback_to_unsolvable, allow_noreturn=True)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 987, in call_function
#     new_node, one_result = func.call(node, funcv, args)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/abstract.py", line 3168, in call
#     node2, ret = self.vm.run_frame(frame, node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 322, in run_frame
#     state = self.run_instruction(op, state)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 287, in run_instruction
#     state = bytecode_fn(state, op)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 2615, in byte_CALL_FUNCTION
#     return self.call_function_from_stack(state, op.arg, None, None)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 1077, in call_function_from_stack
#     state, func, posargs, namedargs, starargs, starstarargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 951, in call_function_with_state
#     starstarargs=starstarargs), fallback_to_unsolvable, allow_noreturn=True)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 987, in call_function
#     new_node, one_result = func.call(node, funcv, args)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/abstract.py", line 3168, in call
#     node2, ret = self.vm.run_frame(frame, node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 322, in run_frame
#     state = self.run_instruction(op, state)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 287, in run_instruction
#     state = bytecode_fn(state, op)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 2025, in byte_LOAD_ATTR
#     state, val = self.load_attr(state, obj, name)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 1261, in load_attr
#     node, result, errors = self._retrieve_attr(state.node, obj, attr)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 1232, in _retrieve_attr
#     node, val.data, attr, val)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/attribute.py", line 59, in get_attribute
#     return self._get_instance_attribute(node, obj, name, valself)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/attribute.py", line 225, in _get_instance_attribute
#     return self._get_attribute(node, obj, obj.cls, name, valself)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/attribute.py", line 275, in _get_attribute
#     attr = self._filter_var(node, attr)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/attribute.py", line 435, in _filter_var
#     bindings.extend(var_bindings)
# AttributeError: 'set' object has no attribute 'extend'