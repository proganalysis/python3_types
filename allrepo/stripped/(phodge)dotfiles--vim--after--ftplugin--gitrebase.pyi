
from typing import Any
def __getattr__(name: Any) -> Any: ...
# Caught error in pytype: Don't know how to match <class 'pytype.pytd.pytd.NamedType'> against <class 'pytype.pytd.pytd.Literal'>
# Traceback (most recent call last):
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 156, in check_or_generate_pyi
#     input_filename=options.input, options=options, loader=loader)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 121, in generate_pyi
#     remove_mutable=False)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/optimize.py", line 1185, in Optimize
#     node = node.Visit(RemoveRedundantSignatures(hierarchy))
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 213, in Visit
#     return _Visit(self, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 241, in _Visit
#     return _VisitNode(node, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 325, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 292, in _VisitNode
#     new_child = _VisitNode(child, visitor, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/parse/node.py", line 343, in _VisitNode
#     new_node = visitor.Visit(new_node, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/pytd_visitors.py", line 184, in Visit
#     self, node, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/optimize.py", line 119, in VisitFunction
#     if self.match.match(s1, s2, self.subst) == booleq.TRUE:
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/pytd_utils.py", line 160, in match
#     return f(t1, t2, *args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/type_match.py", line 450, in match_Signature_against_Signature
#     equalities.append(self.match_type_against_type(p1.type, p2.type, subst))
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/type_match.py", line 309, in match_type_against_type
#     t1, t2, subst)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/type_match.py", line 339, in _match_type_against_type
#     for u in t1.type_list)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/booleq.py", line 371, in And
#     return simplify_exprs(exprs, _And, FALSE, TRUE)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/booleq.py", line 133, in simplify_exprs
#     for e in exprs:
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/type_match.py", line 339, in <genexpr>
#     for u in t1.type_list)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/type_match.py", line 309, in match_type_against_type
#     t1, t2, subst)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/type_match.py", line 358, in _match_type_against_type
#     for t in self.expand_superclasses(t1))
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/booleq.py", line 386, in Or
#     return simplify_exprs(exprs, _Or, TRUE, FALSE)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/booleq.py", line 133, in simplify_exprs
#     for e in exprs:
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/type_match.py", line 358, in <genexpr>
#     for t in self.expand_superclasses(t1))
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/type_match.py", line 309, in match_type_against_type
#     t1, t2, subst)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/pytd/type_match.py", line 396, in _match_type_against_type
#     type(t1), type(t2)))
# AssertionError: Don't know how to match <class 'pytype.pytd.pytd.NamedType'> against <class 'pytype.pytd.pytd.Literal'>