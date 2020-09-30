import abc
from typing import Any, Dict, Generator, List, Union

class UnknownNodeTypeError(Exception): ...

class Node(abc.ABC, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def fields(self) -> List[str]: ...
    def __init__(self, data: Dict[str, Any]) -> None: ...
    def dict(self) -> Dict[str, Any]: ...
    def traverse(self) -> Generator[Node, None, None]: ...
    @property
    def type(self) -> str: ...

def objectify(data: Union[None, Dict[str, Any], List[Dict[str, Any]]]) -> Union[None, Dict[str, Any], List[Any], Node]: ...

class Identifier(Node):
    @property
    def fields(self): ...

class Literal(Node):
    @property
    def fields(self): ...

class Program(Node):
    @property
    def fields(self): ...

class ExpressionStatement(Node):
    @property
    def fields(self): ...

class BlockStatement(Node):
    @property
    def fields(self): ...

class EmptyStatement(Node):
    @property
    def fields(self): ...

class DebuggerStatement(Node):
    @property
    def fields(self): ...

class WithStatement(Node):
    @property
    def fields(self): ...

class ReturnStatement(Node):
    @property
    def fields(self): ...

class LabeledStatement(Node):
    @property
    def fields(self): ...

class BreakStatement(Node):
    @property
    def fields(self): ...

class ContinueStatement(Node):
    @property
    def fields(self): ...

class IfStatement(Node):
    @property
    def fields(self): ...

class SwitchStatement(Node):
    @property
    def fields(self): ...

class SwitchCase(Node):
    @property
    def fields(self): ...

class ThrowStatement(Node):
    @property
    def fields(self): ...

class TryStatement(Node):
    @property
    def fields(self): ...

class CatchClause(Node):
    @property
    def fields(self): ...

class WhileStatement(Node):
    @property
    def fields(self): ...

class DoWhileStatement(Node):
    @property
    def fields(self): ...

class ForStatement(Node):
    @property
    def fields(self): ...

class ForInStatement(Node):
    @property
    def fields(self): ...

class FunctionDeclaration(Node):
    @property
    def fields(self): ...

class VariableDeclaration(Node):
    @property
    def fields(self): ...

class VariableDeclarator(Node):
    @property
    def fields(self): ...

class ThisExpression(Node):
    @property
    def fields(self): ...

class ArrayExpression(Node):
    @property
    def fields(self): ...

class ObjectExpression(Node):
    @property
    def fields(self): ...

class Property(Node):
    @property
    def fields(self): ...

class FunctionExpression(Node):
    @property
    def fields(self): ...

class UnaryExpression(Node):
    @property
    def fields(self): ...

class UpdateExpression(Node):
    @property
    def fields(self): ...

class BinaryExpression(Node):
    @property
    def fields(self): ...

class AssignmentExpression(Node):
    @property
    def fields(self): ...

class LogicalExpression(Node):
    @property
    def fields(self): ...

class MemberExpression(Node):
    @property
    def fields(self): ...

class ConditionalExpression(Node):
    @property
    def fields(self): ...

class CallExpression(Node):
    @property
    def fields(self): ...

class NewExpression(Node):
    @property
    def fields(self): ...

class SequenceExpression(Node):
    @property
    def fields(self): ...
