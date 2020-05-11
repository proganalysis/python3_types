
from typing import Any
def __getattr__(name: Any) -> Any: ...
# Caught error in pytype: Unbound type parameter Feature in FeatureProvider
# Traceback (most recent call last):
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 156, in check_or_generate_pyi
#     input_filename=options.input, options=options, loader=loader)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 113, in generate_pyi
#     analyze.infer_types, input_filename, options, loader)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 65, in wrapper
#     return f(*args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 84, in _call
#     deep=deep)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 670, in infer_types
#     ast = tracer.compute_types(defs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 586, in compute_types
#     return ty.Visit(visitors.AdjustTypeParameters())
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
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 325, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 292, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 325, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 292, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 325, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 292, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 343, in _VisitNode
#     new_node = visitor.Visit(new_node, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/pytd_visitors.py", line 184, in Visit
#     self, node, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/visitors.py", line 1380, in VisitTypeParameter
#     node.name, self._GetFullName(self.constant_name)))
# pytype.pytd.visitors.ContainerError: Unbound type parameter Feature in FeatureProvider