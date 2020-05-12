
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
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 666, in infer_types
#     tracer.exitpoint = tracer.analyze(loc, defs, maximum_depth)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 405, in analyze
#     return self.analyze_toplevel(node, defs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 380, in analyze_toplevel
#     new_node = self.analyze_function(node, value)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 357, in analyze_function
#     node2 = self.maybe_analyze_method(node1, val)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 153, in maybe_analyze_method
#     node, _ = self.call_function_with_args(node, val, args)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 127, in call_function_with_args
#     new_node, ret = self.call_function_in_frame(node, fvar, *args)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 137, in call_function_in_frame
#     state, var, args, kwargs, starargs, starstarargs)
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