from typing import List
import lexer as Lex
import tokens as Tok
import statement as Stm
import expression as Exp


class ParserError(Exception):
    def __init__(self, lineno, msg):
        self.lineno = lineno
        self.msg = msg


class Parser(object):
    def __init__(self):
        self.lex = Lex.Lexer()
        self.path = None
        self.prev_tok = None
        self.this_tok = None
        self.loop_depth = 0
        self.fun_depth = 0

    def parse(self, text):
        self.lex.feed(text)
        self.tok_next()
        return self.program()

    def program(self):
        # program -> statement* "EOF"
        stmts = []
        while not self.tok_is([Tok.EOF]):
            stm = self.declaration()
            stmts.append(stm)
        return stmts

    def declaration(self):
        # declaration -> var_decl ";"
        #              | fun_decl ";"
        #              | statement
        if self.tok_matches(Tok.VAR):
            stm = self.var_decl()
        elif self.tok_matches(Tok.FUN):
            stm = self.fun_decl()
        else:
            stm = self.statement()
        return stm

    def var_decl(self):
        # var_decl -> ^var^ identifier "=" expression ";"
        self.tok_consume(Tok.IDENTIFIER,
                "A variable name should follow the `var` keyword")
        name = self.prev_tok.lexeme
        self.tok_consume(Tok.EQUAL,
                "An equal sign should follow the variable's name")
        value = self.expression()
        self.tok_consume(Tok.SEMICOLON,
                "Missing semicolon after variable declaration")
        return Stm.VarDecl(name, value)

    def fun_decl(self):
        # fun_decl -> ^fun^ identifier "(" formals? ")" block
        # formals  -> identifier ( "," identifier )*
        self.tok_consume(Tok.IDENTIFIER,
                "A function name should follow the `fun` keuyword")
        name = self.prev_tok.lexeme
        self.tok_consume(Tok.PAREN_LEFT,
                "Expected an opening paren after the function name")
        formals = []

        if not self.tok_matches(Tok.PAREN_RIGHT):
            self.tok_consume(Tok.IDENTIFIER,
                    "Function parameters should be a comma-separated list" +
                    "of identifiers")
            formals.append(self.prev_tok.lexeme)

            while self.tok_matches(Tok.COMMA):
                self.tok_consume(Tok.IDENTIFIER,
                        "Function parameters should be a comma-separated " +
                        "list of identifiers")
                formals.append(self.prev_tok.lexeme)
            self.tok_consume(Tok.PAREN_RIGHT,
                    "Expected a closing paren after function arguments")
        self.tok_consume(Tok.DO,
                "Expected a do...end block after function parameter list")
        self.fun_depth += 1
        body = self.block()
        self.fun_depth -= 1

        return Stm.FunDecl(name, formals, body)

    def statement(self):
        # statement -> block
        #            | if_stm
        #            | while_stm
        #            | for_stm
        #            | break_stm
        #            | return_stm
        #            | print_stm
        #            | exp_stm
        if self.tok_matches(Tok.DO):
            stm = self.block()
        elif self.tok_matches(Tok.IF):
            stm = self.if_cond()
        elif self.tok_matches(Tok.WHILE):
            stm = self.while_cond()
        elif self.tok_matches(Tok.FOR):
            stm = self.for_cond()
        elif self.tok_matches(Tok.BREAK):
            stm = self.break_stm()
        elif self.tok_matches(Tok.RETURN):
            stm = self.return_stm()
        elif self.tok_matches(Tok.PRINT):
            stm = self.print_stm()
        else:
            stm = self.exp_stm()

        return stm

    def block(self):
        # block -> ^do^ declaration* "end"
        stmts = []
        while not self.tok_is([Tok.END, Tok.EOF]):
            stm = self.declaration()
            stmts.append(stm)
        self.tok_consume(Tok.END, "Missing `end` keyword after block")
        return Stm.Block(stmts)

    def if_cond(self):
        # if_stm -> ^if^ expression "do" declaration*
        #           ( "elif" expression "do" declaration* )*
        #           ( "else" "do" declaration* )?
        #           "end"
        cond = self.expression()
        self.tok_consume(Tok.DO, "Expected `do` keyword after if condition")
        stmts = []
        while not self.tok_is([Tok.ELIF, Tok.ELSE, Tok.END]):
            stm = self.declaration()
            stmts.append(stm)

        then_block = Stm.Block(stmts)
        else_block = None
        if self.tok_matches(Tok.ELIF):
            else_block = self.if_cond()
        elif self.tok_matches(Tok.ELSE):
            self.tok_consume(Tok.DO,
                    "Expected `do` keywork after else keyword")
            else_block = self.block()
        else:
            self.tok_matches(Tok.END)

        return Stm.If(cond, then_block, else_block)

    def while_cond(self):
        # while_stm -> ^while^ expresion statement
        cond = self.expression()
        self.loop_depth += 1
        body = self.statement()
        self.loop_depth -= 1

        return Stm.While(cond, body)

    def for_cond(self):
        # for_stm -> ^for^ ( var_decl | exp_stm | ";" )
        #                  expression? ";"
        #                  assignment?
        #                  statement
        # NB: var_decl and exp_stm already contain a semicolon
        if self.tok_matches(Tok.VAR):
            init = self.var_decl()
        elif self.tok_matches(Tok.SEMICOLON):
            init = None
        else:
            init = self.exp_stm()

        if not self.tok_matches(Tok.SEMICOLON):
            cond = self.expression()
            self.tok_consume(Tok.SEMICOLON,
                    "Expected a semicolon after the for condition")
        else:
            cond = None

        if not self.tok_matches(Tok.PAREN_RIGHT):
            incr = self.assignment()
        else:
            incr = None

        self.loop_depth += 1
        body = self.statement()
        self.loop_depth -= 1

        if incr is not None:
            incr_stm = Stm.Exp(incr)
            if body.kind == Stm.BLOCK:
                body.block.append(incr_stm)
            else:
                body = Stm.Block([body, incr_stm])

        if cond is None:
            tok = Lex.Token("true", Tok.TRUE, 4, 0, 0)
            cond = Exp.Literal(tok)

        loop = Stm.While(cond, body)

        if init is not None:
            loop = Stm.Block([init, loop])

        return loop

    def break_stm(self):
        # ^break^ ";"
        if self.loop_depth != 0:
            self.tok_consume(Tok.SEMICOLON,
                    "Missing semicolon after break statement")
        else:
            lineno = self.this_tok.lineno
            raise ParserError(lineno,
                              "Encountered break statement outside of a for " +
                              "or while loop")
        return Stm.Break()

    def return_stm(self):
        # return_stm -> ^return^ expression? ";"
        if self.fun_depth != 0:
            if not self.tok_matches(Tok.SEMICOLON):
                ret_exp = self.expression()
                self.tok_consume(Tok.SEMICOLON,
                        "Missing semicolon after return statement")
                return Stm.Return(ret_exp)
            else:
                nil = Lex.Token("nil", Tok.NIL, 3, 0, 0)
                return Stm.Return(Exp.Literal(nil))
        else:
            lineno = self.this_tok.lineno
            raise ParserError(lineno,
                              "Encountered a return statements outside of a " +
                              "function declaration")

    def print_stm(self):
        # print_stm -> ^print^ expression ";"
        exp = self.expression()
        self.tok_consume(Tok.SEMICOLON, "Missing semicolon after print statement")
        return Stm.Print(exp)

    def exp_stm(self):
        # exp_stm -> expression ";"
        exp = self.expression()
        self.tok_consume(Tok.SEMICOLON,
                "Missing semicolon after expression statement")
        return Stm.Exp(exp)

    def expression(self):
        # expression -> assigment
        return self.assignment()

    def assignment(self):
        # assignment -> concat ( "=" assignment )
        left = self.concat()
        if self.tok_matches(Tok.EQUAL):
            right = self.assignment()
            if left.kind == Exp.IDENT:
                return Exp.Assign(left.name, right)
            else:
                lineno = self.this_tok.lineno
                raise ParserError(lineno, "Cannot assign to this target")
        return left

    def concat(self):
        # concat -> or ( "++" or )*
        left = self.logic_or()
        while self.tok_matches(Tok.PLUS_PLUS):
            op = self.prev_tok.kind
            right = self.logic_or()
            left = Exp.Binary(op, left, right)
        return left

    def logic_or(self):
        # or -> and ( "or" and )*
        left = self.logic_and()
        while self.tok_matches(Tok.OR):
            op = self.prev_tok.kind
            right = self.logic_and()
            left = Exp.Binary(op, left, right)
        return left

    def logic_and(self):
        # and -> equality ( "and" equality )*
        left = self.equality()
        while self.tok_matches(Tok.AND):
            op =  self.prev_tok.kind
            right = self.equality()
            left = Exp.Binary(op, left, right)
        return left

    def equality(self):
        # equality -> ordering ( ( "!=" | "==" ) ordering )*
        left = self.ordering()
        while self.tok_matches(Tok.BANG_EQUAL) or \
                self.tok_matches(Tok.EQUAL_EQUAL):
            op = self.prev_tok.kind
            right = self.ordering()
            left = Exp.Binary(op, left, right)
        return left

    def ordering(self):
        # ordering -> addition ( ( ">" | ">=" | "<" | "<=" ) addition )*
        left = self.addition()
        while self.tok_matches(Tok.GREAT) or \
                self.tok_matches(Tok.GREAT_EQUAL) or \
                self.tok_matches(Tok.LESS) or \
                self.tok_matches(Tok.LESS_EQUAL):
            op = self.prev_tok.kind
            right = self.addition()
            left = Exp.Binary(op, left, right)
        return left

    def addition(self):
        # addition -> multiplication ( ( "-" | "+" ) multiplication )*
        left = self.multiplication()
        while self.tok_matches(Tok.MINUS) or \
                self.tok_matches(Tok.PLUS):
            op = self.prev_tok.kind
            right = self.multiplication()
            left = Exp.Binary(op, left, right)
        return left

    def multiplication(self):
        # multiplication -> unary ( ( "/" | "//" | "*" | "%" ) unary )*
        left = self.unary()
        while self.tok_matches(Tok.SLASH) or \
                self.tok_matches(Tok.SLASH_SLASH) or \
                self.tok_matches(Tok.STAR) or \
                self.tok_matches(Tok.PERCENT):
            op = self.prev_tok.kind
            right = self.unary()
            left = Exp.Binary(op, left, right)
        return left

    def unary(self):
        # unary -> ( ( "!" | "-" ) unary )
        #        | call
        if self.tok_matches(Tok.BANG) or self.tok_matches(Tok.MINUS):
            op = self.prev_tok.kind
            exp = self.unary()
            return Exp.Unary(op, exp)
        else:
            return self.call()

    def call(self):
        # call -> primary ( "(" parameters? ")" )*
        callee = self.primary()
        while self.tok_matches(Tok.PAREN_LEFT):
            params = []
            if not self.tok_matches(Tok.PAREN_RIGHT):
                exp = self.expression()
                params.append(exp)
                while self.tok_matches(Tok.COMMA):
                    exp = self.expression()
                    params.append(exp)
                self.tok_consume(Tok.PAREN_RIGHT,
                        "Expected a closing paren after arguments")
            callee = Exp.Call(callee, params)
        return callee

    def primary(self):
        # primary -> IDENTIFIER
        #          | INTEGER | DOUBLE | STRING | NIL | "false" | "true" |
        #          | "(" expression ")"
        if self.tok_matches(Tok.IDENTIFIER):
            exp = Exp.Ident(self.prev_tok.lexeme)
        elif self.tok_matches(Tok.INTEGER) or \
                self.tok_matches(Tok.DOUBLE) or \
                self.tok_matches(Tok.STRING) or \
                self.tok_matches(Tok.NIL) or \
                self.tok_matches(Tok.FALSE) or \
                self.tok_matches(Tok.TRUE):
            exp = Exp.Literal(self.prev_tok)
        elif self.tok_matches(Tok.PAREN_LEFT):
            exp = self.expression()
            self.tok_consume(Tok.PAREN_RIGHT, "Expected a closing paren")
        else:
            lineno = self.this_tok.lineno
            raise ParserError(lineno,
                              "Expected number, paren or keyword. Got " +
                              str(self.this_tok))
        return exp

    def tok_next(self):
        self.prev_tok = self.this_tok
        self.this_tok = self.lex.get_tok()
        return self.prev_tok

    def tok_matches(self, kind):
        if self.this_tok.kind == kind:
            self.tok_next()
            return True
        else:
            return False

    def tok_consume(self, kind, message):
        if self.this_tok.kind == kind:
            self.tok_next()
        else:
            lineno = self.this_tok.lineno
            raise ParserError(lineno, message)

    def tok_is(self, kind_arr: List) -> bool:
        return any(map(lambda x: x == self.this_tok.kind, kind_arr))

    def tok_was(self, kind):
        return self.prev_tok.kind == kind
