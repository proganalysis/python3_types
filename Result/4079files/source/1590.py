import tokens as Tok

keywords = {
    "and"   : Tok.AND,
    "break" : Tok.BREAK,
    "do"    : Tok.DO,
    "elif"  : Tok.ELIF,
    "else"  : Tok.ELSE,
    "end"   : Tok.END,
    "false" : Tok.FALSE,
    "for"   : Tok.FOR,
    "fun"   : Tok.FUN,
    "if"    : Tok.IF,
    "nil"   : Tok.NIL,
    "or"    : Tok.OR,
    "print" : Tok.PRINT,
    "return": Tok.RETURN,
    "true"  : Tok.TRUE,
    "var"   : Tok.VAR,
    "while" : Tok.WHILE
}


def is_alpha(char: str) -> bool:
    return ("a" <= char <= "z") or \
           ("A" <= char <= "Z") or\
            char == "_"


def is_numeric(char: str) -> bool:
    return "0" <= char <= "9"


def is_alpha_num(char: str) -> bool:
    return is_alpha(char) or is_numeric(char)


class LexerError(Exception):
    def __init__(self, msg, lineno):
        self.msg = msg
        self.lineno = lineno


class Token():
    def __init__(self, lexeme, kind, length, lineno, colno):
        self.lexeme = lexeme
        self.kind = kind
        self.length = length
        self.lineno = lineno
        self.colno = colno

    def __repr__(self, bare=True):
        if bare:
            return self.lexeme
        else:
            return "(%s @ %i %i)" % (self.lexeme, self.lineno, self.colno)


class Lexer():
    def __init__(self):
        self.buffer = None
        self.index = 0
        self.start = 0
        self.lineno = 1
        self.colno = 0

    def feed(self, buf):
        self.index = 0
        self.buffer = buf

    def char_next(self) -> str:
        char = self.buffer[self.index]
        self.index += 1
        self.colno += 1
        return char

    def lookahead(self) -> str:
        return self.buffer[self.index]

    def is_at_end(self) -> bool:
        return self.buffer[self.index] == '\0'

    def char_matches(self, char: str) -> bool:
        if self.is_at_end():
            return False
        elif self.buffer[self.index] == char:
            self.char_next()
            return True
        else:
            return False

    def skip_space(self):
        while True:
            char = self.lookahead()
            if char in " \r\t":
                self.char_next()
            elif char == "\n":
                self.lineno += 1
                self.colno = 0
                self.char_next()
            else:
                break

    def skip_line(self):
        while True:
            char = self.lookahead()
            if char == "\n":
                self.lineno += 1
                self.colno = 0
                self.char_next()
                break
            elif char == '\0':
                break
            else:
                self.char_next()

    def get_tok(self) -> Token:
        self.skip_space()
        self.start = self.index
        char = self.char_next()

        if is_alpha(char):
            return self.identifier()
        if is_numeric(char):
            return self.number()

        if char == "!":
            if self.char_matches("="):
                return self.tok(Tok.BANG_EQUAL)
            else:
                return self.tok(Tok.BANG)
        elif char == ",":
            return self.tok(Tok.COMMA)
        elif char == "=":
            if self.char_matches("="):
                return self.tok(Tok.EQUAL_EQUAL)
            else:
                return self.tok(Tok.EQUAL)
        elif char == ">":
            if self.char_matches("="):
                return self.tok(Tok.GREAT_EQUAL)
            else:
                return self.tok(Tok.GREAT)
        elif char == "#":
            self.skip_line()
            return self.get_tok()
        elif char == "<":
            if self.char_matches("="):
                return self.tok(Tok.LESS_EQUAL)
            else:
                return self.tok(Tok.LESS)
        elif char == "-":
            return self.tok(Tok.MINUS)
        elif char == "(":
            return self.tok(Tok.PAREN_LEFT)
        elif char == ")":
            return self.tok(Tok.PAREN_RIGHT)
        elif char == "%":
            return self.tok(Tok.PERCENT)
        elif char == "+":
            if self.char_matches("+"):
                return self.tok(Tok.PLUS_PLUS)
            else:
                return self.tok(Tok.PLUS)
        elif char == "\"":
            return self.string()
        elif char == ";":
            return self.tok(Tok.SEMICOLON)
        elif char == "/":
            if self.char_matches("/"):
                return self.tok(Tok.SLASH_SLASH)
            else:
                return self.tok(Tok.SLASH)
        elif char == "*":
            return self.tok(Tok.STAR)
        elif char == "\0":
            return self.tok(Tok.EOF)
        else:
            raise LexerError("Unknown character: '%s'" % char, self.lineno)

    def tok(self, kind) -> Token:
        lexeme = self.buffer[self.start:self.index]
        length = self.index - self.start
        return Token(lexeme, kind, length, self.lineno, self.colno - length)

    def identifier(self) -> Token:
        while is_alpha_num(self.lookahead()):
            self.char_next()

        tok = self.tok(Tok.IDENTIFIER)
        if tok.lexeme in keywords:
            tok.kind = keywords[tok.lexeme]

        return tok

    def number(self) -> Token:
        is_double = False

        while True:
            if is_numeric(self.lookahead()):
                self.char_next()
            elif self.lookahead() == ".":
                if not is_double:
                    is_double = True
                    self.char_next()
                else:
                    break
            else:
                break

        if is_double:
            return self.tok(Tok.DOUBLE)
        else:
            return self.tok(Tok.INTEGER)

    def string(self) -> Token:
        self.start = self.index
        while self.lookahead() != "\"":
            self.char_next()
        tok = self.tok(Tok.STRING)
        self.char_next()
        return tok
