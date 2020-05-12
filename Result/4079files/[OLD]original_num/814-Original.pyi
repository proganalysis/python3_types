
from typing import Any
def __getattr__(name: Any) -> Any: ...
# Caught error in pytype: Duplicate name(s) ['OrderedDict'] in both constants and type_params
# Traceback (most recent call last):
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 156, in check_or_generate_pyi
#     input_filename=options.input, options=options, loader=loader)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 114, in generate_pyi
#     mod.Visit(visitors.VerifyVisitor())
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 213, in Visit
#     return _Visit(self, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 241, in _Visit
#     return _VisitNode(node, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 314, in _VisitNode
#     status = visitor.Enter(node, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/visitors.py", line 944, in Enter
#     super(VerifyVisitor, self).Enter(node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/pytd_visitors.py", line 180, in Enter
#     self, node, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/visitors.py", line 963, in EnterTypeDeclUnit
#     "functions", "aliases"])
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/visitors.py", line 959, in _AssertNoDuplicates
#     list(both), a1, a2))
# AssertionError: Duplicate name(s) ['OrderedDict'] in both constants and type_params