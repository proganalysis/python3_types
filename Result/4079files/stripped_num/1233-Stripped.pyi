# (generated with --quick)

import __builtin__
import collections
from typing import Any, Generator, List, Type

OrderedDict: Type[collections.OrderedDict]
abc: module

class ArrayExpression(Node):
    fields: List[str]

class AssignmentExpression(Node):
    fields: List[str]

class BinaryExpression(Node):
    fields: List[str]

class BlockStatement(Node):
    fields: List[str]

class BreakStatement(Node):
    fields: List[str]

class CallExpression(Node):
    fields: List[str]

class CatchClause(Node):
    fields: List[str]

class ConditionalExpression(Node):
    fields: List[str]

class ContinueStatement(Node):
    fields: List[str]

class DebuggerStatement(Node):
    fields: List[nothing]

class DoWhileStatement(Node):
    fields: List[str]

class EmptyStatement(Node):
    fields: List[nothing]

class ExpressionStatement(Node):
    fields: List[str]

class ForInStatement(Node):
    fields: List[str]

class ForStatement(Node):
    fields: List[str]

class FunctionDeclaration(Node):
    fields: List[str]

class FunctionExpression(Node):
    fields: List[str]

class Identifier(Node):
    fields: List[str]

class IfStatement(Node):
    fields: List[str]

class LabeledStatement(Node):
    fields: List[str]

class Literal(Node):
    fields: List[str]

class LogicalExpression(Node):
    fields: List[str]

class MemberExpression(Node):
    fields: List[str]

class NewExpression(Node):
    fields: List[str]

class Node(abc.ABC):
    __doc__: str
    fields: Any
    type: Any
    def __init__(self, data) -> None: ...
    def dict(self) -> __builtin__.dict: ...
    def traverse(self) -> Generator[Node, Any, None]: ...

class ObjectExpression(Node):
    fields: List[str]

class Program(Node):
    fields: List[str]

class Property(Node):
    fields: List[str]

class ReturnStatement(Node):
    fields: List[str]

class SequenceExpression(Node):
    fields: List[str]

class SwitchCase(Node):
    fields: List[str]

class SwitchStatement(Node):
    fields: List[str]

class ThisExpression(Node):
    fields: List[nothing]

class ThrowStatement(Node):
    fields: List[str]

class TryStatement(Node):
    fields: List[str]

class UnaryExpression(Node):
    fields: List[str]

class UnknownNodeTypeError(Exception):
    __doc__: str

class UpdateExpression(Node):
    fields: List[str]

class VariableDeclaration(Node):
    fields: List[str]

class VariableDeclarator(Node):
    fields: List[str]

class WhileStatement(Node):
    fields: List[str]

class WithStatement(Node):
    fields: List[str]

def objectify(data) -> Any: ...
