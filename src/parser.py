from nodes import (
    ProgramStatement,
    BinaryExpression,
    NumericLiteral,
    Identifier,
    VariableDeclarationStatement,
    AssignmentExpression,
    PrintStatement
)

from error import LynxError
from Token import TokenType

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

        self.idx = 0

        self.semiafterexpr = True

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
        
        return tok

    def atEnd(self):
        return self.peek().type == TokenType.EOF
    
    def parse(self):
        program = ProgramStatement()

        while not self.atEnd():
            program.statements.append(self.parseStatement())

        return program
    
    def parseConstVarDeclaration(self):
        tok = self.eat()

        id = self.expect(TokenType.identifier, "Expected identifier in variable declaration.")
        id = Identifier(id, id.pos.line, id.pos.col)

        self.expect(TokenType.equals, "Expected equals sign in constant variable declaration.")

        init = self.parseExpression()

        self.expect(TokenType.semi, "Expected semicolon at end of variable declaration statement.")

        return VariableDeclarationStatement(id, init, "const", tok.pos.line, tok.pos.col)


    def parseVariableDeclaration(self):
        if self.peek().type == TokenType._const:
            return self.parseConstVarDeclaration()
        tok = self.expect(TokenType._var, "Expected var keyword at beginning of variable declaration.")

        id = self.expect(TokenType.identifier, "Expected identifier in variable declaration.")
        id = Identifier(id, id.pos.line, id.pos.col)

        if self.peek().type == TokenType.semi: # uninitialized variable
            self.eat()
            return VariableDeclarationStatement(id, None, "var", tok.pos.line, tok.pos.col)
        
        self.expect(TokenType.equals, "Expected equals sign or semicolon after identifier in variable declaration.")

        init = self.parseExpression()

        self.expect(TokenType.semi, "Expected semicolon at end of variable declaration statement.")

        return VariableDeclarationStatement(id, init, "var", tok.pos.line, tok.pos.col)
    
    def parsePrintStatement(self):
        tok = self.eat()

        argument = self.parseExpression()

        self.expect(TokenType.semi, "Expected semicolon at end of print statement")

        return PrintStatement(argument, tok.pos.line, tok.pos.col)
    
    def parseStatement(self):
        if self.peek().type == TokenType._var or self.peek().type == TokenType._const:
            return self.parseVariableDeclaration()
        elif self.peek().type == TokenType._print:
            return self.parsePrintStatement()
        else:
            expr = self.parseExpression()
            if self.semiafterexpr:
                self.expect(TokenType.semi, "Expected semicolon after standalone expression.")
            return expr
    
    def parseExpression(self):
        return self.parseAssignment()
    
    def parseAssignment(self):
        left = self.parseAdditive()

        if self.peek().type == TokenType.equals:
            self.eat()
            right = self.parseAssignment()
            return AssignmentExpression(left, right, left.pos.line, left.pos.col)
        
        return left

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
        elif tok.type == TokenType.identifier:
            self.eat()
            # token used for position in enviornment
            return Identifier(tok, tok.pos.line, tok.pos.col)
        elif tok.type == TokenType.leftParen:
            self.eat()
            value = self.parseExpression()
            self.expect(TokenType.rightParen, "Expected a closing parenthesis to conclude grouped expression")
            return value
        else:
            raise LynxError(f"Unexpected token: '{tok.type}'", tok.pos.line, tok.pos.col)


    

