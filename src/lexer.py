import error

class TokenType:
    leftParen = "leftParen"
    rightParen = "rightParen"
    plus = "plus"
    minus = "minus"
    mult = "mult"
    divide = "divide"
    number = "number"
    EOF = "EOF"

class Token:
    def __init__(self, type, line, col, value=None):
        self.type = type
        self.value = value

        self.line = line
        self.col = col


    def __repr__(self):
        if self.value:
            return f"Token({self.type}, {self.value})"
        else:
            return f"Token({self.type})"

class Lexer:
    def __init__(self, src):
        self.src = src

        self.idx = 0

        self.line = 1
        self.col = 1

        self.tokens = []

    def peek(self):
        return self.src[self.idx]
    
    def eat(self):
        char = self.peek()

        self.idx += 1

        if char == "\n":
            self.line += 1
            self.col = 1
        else:
            self.col += 1

        return char
    
    def atEnd(self):
        return self.idx >= len(self.src)
    
    def scanToken(self):
        if self.peek() == "(":
            self.eat()
            return Token(TokenType.leftParen, self.line, self.col)
        elif self.peek() == ")":
            self.eat()
            return Token(TokenType.rightParen, self.line, self.col)
        elif self.peek() == "+":
            self.eat()
            return Token(TokenType.plus, self.line, self.col)
        elif self.peek() == "-":
            self.eat()
            return Token(TokenType.minus, self.line, self.col)
        elif self.peek() == "*":
            self.eat()
            return Token(TokenType.mult, self.line, self.col)
        elif self.peek() == "/":
            self.eat()
            return Token(TokenType.divide, self.line, self.col)
        elif self.peek().isnumeric():
            number = self.eat()
            while not self.atEnd() and self.peek().isnumeric():
                number += self.eat()

            return Token(TokenType.number, self.line, self.col,int(number))
        elif self.peek() in "\t ":
            self.eat()
        else:
            raise error.LynxError(f"Unrecognized character in source: '{self.peek()}'", self.line, self.col)

    def tokenize(self):
        while not self.atEnd():
            tok = self.scanToken()
            if tok:
                self.tokens.append(tok)
        
        self.tokens.append(Token(TokenType.EOF, self.line, self.col))
        return self.tokens