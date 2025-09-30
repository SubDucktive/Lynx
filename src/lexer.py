import error
from Token import TokenType, Token

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
        line, col = self.line, self.col
        if self.peek() == "(":
            self.eat()
            return Token(TokenType.leftParen, line, col)
        elif self.peek() == ")":
            self.eat()
            return Token(TokenType.rightParen, line, col)
        elif self.peek() == "+":
            self.eat()
            return Token(TokenType.plus, line, col)
        elif self.peek() == "-":
            self.eat()
            return Token(TokenType.minus, line, col)
        elif self.peek() == "*":
            self.eat()
            return Token(TokenType.mult, line, col)
        elif self.peek() == "/":
            self.eat()

            if not self.atEnd() and self.peek() == "/":
                # comment
                while not self.atEnd() and self.peek() != "\n":
                    self.eat()

                return

            return Token(TokenType.divide, line, col)
        elif self.peek() == "=":
            self.eat()
            return Token(TokenType.equals, line, col)
        elif self.peek() == ";":
            self.eat()
            return Token(TokenType.semi, line, col)
        elif self.peek() == "&":
            self.eat()

            if not self.atEnd() and self.peek() == "&":
                self.eat()
                return Token(TokenType.logand, line, col)
            
            return Token(TokenType.bitand, line, col)
        elif self.peek() == "|":
            self.eat()

            if not self.atEnd() and self.peek() == "|":
                self.eat()
                return Token(TokenType.logor, line, col)
            
            return Token(TokenType.bitor, line, col)
        elif self.peek() == "{":
            self.eat()
            return Token(TokenType.leftBrace, line, col)
        elif self.peek() == "}":
            self.eat()
            return Token(TokenType.rightBrace, line, col)
        elif self.peek().isnumeric():
            number = self.eat()
            while not self.atEnd() and self.peek().isnumeric():
                number += self.eat()

            return Token(TokenType.number, line, col, int(number))
        elif self.peek().isalpha() or self.peek() == "_":
            symbol = self.eat()

            while not self.atEnd() and (self.peek().isalnum() or self.peek() == "_"):
                symbol += self.eat()

            if symbol == "var":
                return Token(TokenType._var, line, col, symbol)
            elif symbol == "print":
                return Token(TokenType._print, line, col, symbol)
            elif symbol == "const":
                return Token(TokenType._const, line, col, symbol)
            elif symbol == "null":
                return Token(TokenType._null, line, col, symbol)

            return Token(TokenType.identifier, line, col, symbol)
        elif self.peek() in "\t ":
            self.eat()
        elif self.peek() == "\n":
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