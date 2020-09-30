from typing import List
import statement as Stm
import expression as Exp
import tokens as Tok


class Break(BaseException):
    pass


class Return(BaseException):
    def __init__(self, val):
        self.val = val


class RuntimeError(BaseException):
    def __init__(self, lineno, msg):
        self.lineno = lineno
        self.msg = msg


class Environment(object):
    def __init__(self, parent=None):
        self.parent = parent
        self.values = {}

    def __getitem__(self, key: str):
        if key in self.values:
            return self.values[key]
        elif self.parent is not None:
            return self.parent[key]
        else:
            raise Exception("Undeclared variable: " + key)

    def __setitem__(self, key, value):
        if key in self.values:
            self.values[key] = value
        elif self.parent is not None:
            self.parent[key] = value
        else:
            raise Exception("Undeclared variable: " + key)

    def __str__(self):
        res = str(self.values) + "\n" + str(self.parent)
        return res

    def getAt(self, distance: int, name: str):
        context = self
        for i in range(distance):
            context = context.parent
        return context.values[name]

    def setAt(self, distance: int, name: str, val):
        context = self
        for i in range(distance):
            context = context.parent
        context.values[name] = val

    def declare(self, key, value):
        if key not in self.values:
            self.values[key] = value
        else:
            raise Exception("Redeclaring variable: " + key)


class Interpreter(object):
    def __init__(self):
        self.globals = Environment(None)
        self.context = self.globals
        self.locals = {} # Dict[Exp, int]

    def enterScope(self):
        self.context = Environment(self.context)

    def exitScope(self):
        self.context = self.context.parent

    def resolve(self, exp: Exp, depth: int):
        self.locals[exp] = depth

    def lookUpVariable(self, name: str, exp: Exp):
        if exp in self.locals:
            distance = self.locals[exp]
            return self.context.getAt(distance, name)
        else:
            return self.globals[name]

    def interpret(self, ast: List[Stm.Stm]):
        # XXX runtime errors should be caught here
        for stm in ast:
            self.execute(stm)

    # Statement handling
    def execute(self, stm: Stm.Stm):
        stm.accept(self)

    def contextualExecute(self, stmts: List[Stm.Stm], ctx: Environment):
        prev_ctx = self.context
        self.context = ctx
        try:
            for stm in stmts:
                self.execute(stm)
        finally:
            self.context = prev_ctx

    def visitStmVarDecl(self, stm: Stm.VarDecl):
        val = self.evaluate(stm.exp)
        self.context.declare(stm.name, val)

    def visitStmFunDecl(self, stm: Stm.FunDecl):
        fun = Function(stm.formals, self.context, stm.body)
        self.context.declare(stm.name, fun)

    def visitStmBlock(self, stm: Stm.Block):
        self.enterScope()
        for stm in stm.block:
            self.execute(stm)
        self.exitScope()

    def visitStmIf(self, stm: Stm.If):
        cond = self.evaluate(stm.cond)
        if is_truthy(cond):
            self.execute(stm.then_block)
        elif stm.else_block is not None:
            self.execute(stm.else_block)

    def visitStmWhile(self, stm: Stm.While):
        startCtx = self.context
        try:
            while is_truthy(self.evaluate(stm.cond)):
                self.execute(stm.body)
        except Break:
            while self.context != startCtx:
                self.exitScope()

    def visitStmBreak(self, stm: Stm.Break):
        raise Break

    def visitStmReturn(self, stm: Stm.Return):
        val = self.evaluate(stm.ret_exp)
        raise Return(val)

    def visitStmPrint(self, stm: Stm.Print):
        val = self.evaluate(stm.print_exp)
        print(stringify(val))

    def visitStmExp(self, stm: Stm.Exp):
        self.evaluate(stm.exp)

    # Expression handling
    def evaluate(self, exp: Exp.Exp):
        return exp.accept(self)

    def visitExpAssign(self, exp: Exp.Assign):
        val = self.evaluate(exp.exp)
        if exp in self.locals:
            distance = self.locals[exp]
            self.context.setAt(distance, exp.name, val)
        else:
            self.globals[exp.name] = val
        return val

    def visitExpBinary(self, exp: Exp.Binary):
        left = self.evaluate(exp.left)
        right = self.evaluate(exp.right)
        if are_compat(exp.op, left, right):
            if exp.op == Tok.PLUS:
                return left + right
            elif exp.op == Tok.MINUS:
                return left - right
            elif exp.op == Tok.SLASH:
                return left / right
            elif exp.op == Tok.SLASH_SLASH:
                return left // right
            elif exp.op == Tok.STAR:
                return left * right
            elif exp.op == Tok.PERCENT:
                return left % right
            elif exp.op == Tok.GREAT:
                return left > right
            elif exp.op == Tok.GREAT_EQUAL:
                return left >= right
            elif exp.op == Tok.LESS:
                return left < right
            elif exp.op == Tok.LESS_EQUAL:
                return left <= right
            elif exp.op == Tok.EQUAL_EQUAL:
                return left == right
            elif exp.op == Tok.BANG_EQUAL:
                return left != right
            elif exp.op == Tok.AND:
                if is_truthy(left):
                    return right
                else:
                    return left
            elif exp.op == Tok.OR:
                if not is_truthy(left):
                    return right
                else:
                    return left
            elif exp.op == Tok.PLUS_PLUS:
                return stringify(left) + stringify(right)
        else:
            raise Exception("type mismatch %s <> %s" %
                            (type(left), type(right)))


    def visitExpUnary(self, exp: Exp.Unary):
        val = self.evaluate(exp.exp)
        if exp.op == Tok.MINUS:
            if not is_num(val):
                raise Exception("passed non-num to unary")
            else:
                return -val
        elif exp.op == Tok.BANG:
            return not is_truthy(val)

    def visitExpCall(self, exp: Exp.Call):
        args = []
        for arg in exp.params:
            args.append(self.evaluate(arg))
        fun = self.evaluate(exp.callee)

        if isinstance(fun, Function):
            return fun.call(self, args)
        else:
            raise Exception("Attempted to call non-function")

    def visitExpIdent(self, exp: Exp.Ident):
        return self.lookUpVariable(exp.name, exp)

    def visitExpLiteral(self, exp: Exp.Literal):
        kind = exp.tok.kind
        lexeme = exp.tok.lexeme
        if kind == Tok.NIL:
            return None
        elif kind == Tok.FALSE:
            return False
        elif kind == Tok.TRUE:
            return True
        elif kind == Tok.INTEGER:
            return int(lexeme)
        elif kind == Tok.DOUBLE:
            return float(lexeme)
        elif kind == Tok.STRING:
            return lexeme

def is_num(val) -> bool:
    return isinstance(val, int) or isinstance(val, float)

def are_compat(op, left, right) -> bool:
    if op in Tok.algebra:
        return is_num(left) and is_num(right)
    elif op in Tok.compare:
        return (is_num(left) and is_num(right)) or\
               (isinstance(left, str) and isinstance(right, str))
    else:
        return True

def is_truthy(val) -> bool:
    if val == False:
        return False
    else:
        return True

def stringify(val) -> str:
    if val is None:
        return "nil"
    elif val is False:
        return "false"
    elif val is True:
        return "true"
    else:
        return str(val)


class Function(object):
    def __init__(self,
                 params: List[str],
                 closure: Environment,
                 body: Stm.Block):
        self.params = params
        self.closure = closure
        self.body = body

    def call(self, intpr: Interpreter, args: List):
        this_ctx = Environment(self.closure)
        for name, value in zip(self.params, args):
            this_ctx.declare(name, value)

        val = None
        try:
            intpr.contextualExecute(self.body.block, this_ctx)
        except Return as ret:
            val = ret.val
        return val
