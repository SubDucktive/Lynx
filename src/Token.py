from position import Position

class TokenType:
    leftParen = "leftParen"
    rightParen = "rightParen"
    plus = "plus"
    minus = "minus"
    mult = "mult"
    divide = "divide"
    number = "number"
    identifier = "identifier"
    equals = "equals"
    semi = "semi"

    logand = "logand"
    logor  = "logor"

    bitand = "bitand"
    bitor  = "bitor"
    bitxor = "bitxor"

    leftBrace, rightBrace = "leftBrace", "rightBrace"

    # keywords
    _var = "var"
    _print = "print"
    _const = "const"
    _null = "null"

    EOF = "EOF"

class Token:
    def __init__(self, type, line, col, value=None):
        self.type = type
        self.value = value

        self.pos = Position(line, col)

    def __repr__(self):
        if self.value:
            return f"Token({self.type}, '{self.value}')"
        else:
            return f"Token({self.type})"