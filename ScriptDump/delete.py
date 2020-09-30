TyDp = ["attribute-error","wrong-arg-types","unsupported-operands","bad-return-type","key-error","not-callable","not-writable","not-indexable"]
TySha = ["wrong-arg-count","ignored-abstractmethod","missing-parameter","wrong-keyword-args","mro-error","ignored-metaclass","bad-unpacking","duplicate-keyword-argument","annotation-type-mismatch","not-instantiable","base-class-error","invalid-function-definition","invalid-super-call","bad-slots","bad-concrete-type","recursion-error"]
TySyn = ["python-compiler-error","invalid-annotation","invalid-type-comment","invalid-typevar","ignored-type-comment","invalid-function-type-comment","invalid-namedtuple-arg","redundant-function-type-comment"]
TyImp = ["import-error","name-error","module-attr","pyi-error","not-supported-yet","reveal-type"]

MyDp = ["attr-defined","assignment","var-annotated","arg-type","union-attr","return-value","index","operator","override","list-item","dict-item","type-var"]
MySha = ["no-redef","call-arg","has-type","return","call-overload","str-format","func-returns-value","type-arg","str-bytes-safe","abstract","exit-return","valid-newtype"]
MySyn = ["valid-type","syntax"]
MyImp = ["name-defined","misc"]




"""
from typing import List

a: List[str] = [1]
b = a[0]
c = b + 1
reveal_type(a)
reveal_type(b)
reveal_type(c)
reveal_type(a[0])
#reveal_type(a)

"""
"""
a: str = "ab"
b: int = 5
reveal_type(b)
b = a
reveal_type(a)
reveal_type(b)

c = []
c.append("AAA")
reveal_type(c)
c.append(9)
reveal_type(c)

"""

"""
def g(a:int) -> int:
	return a * 2

def f(a:str) -> int:
	b = a + 2
	d = g("ei")
	return "abc"



"""
"""
def f(a:int) -> str:
	return 5
class GenericResource():	
	def __init__(self, _class: str=None):
		self.__class = _class

	def _class(self) -> str:
	    reveal_type(self.__class)
	    return self.__class	
"""
"""
a = [print("bew")]
print(a)
"""
"""
a = 10
b = sqrt(a)
print(b)
"""
"""
a = {"Ant","Bat","Cat"}
b = "#".join()

print(b)
"""
"""
import re
p = ["Asd",
"Asd"]
a =  "Dict[str, Dict[str, U'ni'on[str, bytes]](Aasd)]"
b = re.split('\[|\]|,|\(|\)|\'', a)
for x in range(len(b)):
	c = b[x].strip()
	if c != "":
		print(c)
"""
"""
string = "123"
#if '+' in string:
if string == "wut":
    split_modifier = string.split('+')
    #split_modifier[-1] = int(split_modifier[-1])
else:
    split_modifier = [string, 0]
"""
"""
a = ["a", "b"]
a = ["c", 5]
reveal_type(a)
print(a)
"""
"""
if "as" in c:
	b = "ASD"
	a = b.split(',')
else:
	a = [c, 5]

print(a)
"""