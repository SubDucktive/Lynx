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
    colon = "colon"

    equalto = "equalto"
    notequal = "notequal"

    lessthan = "lessthan"
    greaterthan = "greaterthan"

    lessequal = "lessequal"
    greaterequal = "greaterequal"

    logand = "logand"
    logor  = "logor"

    lognot = "lognot"

    bitand = "bitand"
    bitor  = "bitor"
    bitxor = "bitxor"

    leftBrace = "leftBrace"
    rightBrace = "rightBrace"

    # keywords
    _var = "var"
    _print = "print"
    _const = "const"
    _null = "null"
    _if = "if"
    _else = "else"

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

    def dict(self):
        return {
            "type": self.type,
            "value": self.value,
            "pos": self.pos.dict()
        }