from position import Position

class ProgramStatement:
    def __init__(self):
        self.type = "ProgramStatement"
        self.statements = []

        self.pos = Position(1, 1)

    def dict(self):
        return {
            "type": self.type,
            "statements": [stmt.dict() for stmt in self.statements],
            "self.pos": self.pos.dict()
        }

class VariableDeclarationStatement:
    def __init__(self, id, init, kind, line, col):
        self.type = "VariableDeclarationStatement"

        self.id = id
        self.init = init

        self.kind = kind

        self.pos = Position(line, col)

    def dict(self):
        return {
            "type": self.type,
            "id": self.id.dict(),
            "init": self.init.dict(),
            "kind": self.kind,
            "pos": self.pos.dict()
        }
    
class PrintStatement:
    def __init__(self, argument, line, col):
        self.type = "PrintStatement"

        self.argument = argument

        self.pos = Position(line, col)

    def dict(self):
        return {
            "type": self.type,
            "argument": self.argument.dict(),
            "pos": self.pos.dict()
        }

class NumericLiteral:
    def __init__(self, value, line, col):
        self.type = "NumericLiteral"

        self.value = value

        self.pos = Position(line, col)

    def dict(self):
        return {
            "type": self.type,
            "value": self.value,
            "pos": self.pos.dict()
        }

class Identifier:
    def __init__(self, name, line, col):
        self.type = "Identifier"

        self.name = name

        self.pos = Position(line, col)
        
    def dict(self):
        return {
            "type": self.type,
            "name": self.name,
            "pos": self.pos.dict()
        }

class BinaryExpression:
    def __init__(self, left, op, right, line, col):
        self.type = "BinaryExpression"

        self.left = left
        self.op = op
        self.right = right

        self.pos = Position(line, col)

    def dict(self):
        return {
            "type": self.type,
            "left": self.left.dict(),
            "op": str(self.op),
            "right": self.right.dict(),
            "pos": self.pos.dict()
        }
    
class AssignmentExpression():
    def __init__(self, left, right, line, col):
        self.type = "AssignmentExpression"

        self.left = left
        self.right = right

        self.pos = Position(line, col)

    def dict(self):
        return {
            "type": self.type,
            "left": self.left.dict(),
            "right": self.right.dict(),
            "pos": self.pos.dict()
        }