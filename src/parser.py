from nodes import (
    ProgramStatement,
    BinaryExpression,
    NumericLiteral
)

from error import LynxError
from Token import TokenType

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

        self.idx = 0

    def peek(self):
        return self.tokens[self.idx]

    def eat(self):
        tok = self.peek()
        self.idx += 1
        return tok
    
    def expect(self, type, message):
        tok = self.eat()
        if tok.type != type:
            raise LynxError(message, tok.pos.line, tok.pos.col)

    def atEnd(self):
        return self.peek().type == TokenType.EOF
    
    def parse(self):
        program = ProgramStatement()

        while not self.atEnd():
            program.statements.append(self.parseStatement())

        return program

    def parseStatement(self):
        return self.parseExpression()
    
    def parseExpression(self):
        return self.parseAdditive()

    def parseAdditive(self):
        left = self.parseMultiplicative()

        while self.peek().type in [TokenType.plus, TokenType.minus]:
            op = self.eat()
            right = self.parseMultiplicative()
            left = BinaryExpression(left, op, right, left.pos.line, left.pos.col)

        return left

    def parseMultiplicative(self):
        left = self.parsePrimary()

        while self.peek().type in [TokenType.mult, TokenType.divide]:
            op = self.eat()
            right = self.parsePrimary()
            left = BinaryExpression(left, op, right, left.pos.line, left.pos.col)

        return left

    def parsePrimary(self):
        tok = self.peek()
        if tok.type == TokenType.number:
            self.eat()
            return NumericLiteral(tok.value, tok.pos.line, tok.pos.col)
        elif tok.type == TokenType.leftParen:
            self.eat()
            value = self.parseExpression()
            self.expect(TokenType.rightParen, "Expected a closing parenthesis to conclude grouped expression")
            return value
        else:
            raise LynxError(f"Unexpected token: '{tok.type}'", tok.pos.line, tok.pos.col)


    

