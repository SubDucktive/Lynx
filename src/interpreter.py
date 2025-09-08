import runtimevalues
import error
from Token import TokenType

def evaluate(node, env):
    if node.type == "ProgramStatement":
        lastEvaluated = None

        for statement in node.statements:
            lastEvaluated = evaluate(statement, env)
        
        return lastEvaluated
    elif node.type == "NumericLiteral":
        return runtimevalues.Number(node.value)
    elif node.type == "BinaryExpression":
        lhs = evaluate(node.left, env)
        rhs = evaluate(node.right, env)

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
    elif node.type == "Identifier":
        return env.lookup(node.name)
    elif node.type == "VariableDeclarationStatement":
        init = evaluate(node.init, env)
        env.defineVariable(node.id.name, init)
