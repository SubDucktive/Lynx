import runtimevalues
import error
from Token import TokenType

def evaluate(node):
    if node.type == "ProgramStatement":
        lastEvaluated = None

        for statement in node.statements:
            lastEvaluated = evaluate(statement)
        
        return lastEvaluated
    elif node.type == "NumericLiteral":
        return runtimevalues.Number(node.value)
    elif node.type == "BinaryExpression":
        lhs = evaluate(node.left)
        rhs = evaluate(node.right)

        result = 0

        if node.op.type == TokenType.plus:
            result = lhs.value + rhs.value
        elif node.op.type == TokenType.minus:
            result = lhs.value - rhs.value
        elif node.op.type == TokenType.mult:
            result = lhs.value * rhs.value
        elif node.op.type == TokenType.divide:
            if rhs.value == 0:
                result = 0
            else:
                result = lhs.value / rhs.value

        return runtimevalues.Number(result)