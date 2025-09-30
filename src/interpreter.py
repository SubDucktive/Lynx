import runtimevalues
import error
import enviornment
from Token import TokenType

# will be very useful for later
def stringify(value):
    if value is not None:
        if value.type in ["NumberValue", "NullValue"]:
            return value.value
        elif value.type == "BooleanValue":
            return "true" if value.value else "false"
    return ""

def evaluate(node, env):
    if node.type == "ProgramStatement":
        lastEvaluated = None

        for statement in node.statements:
            lastEvaluated = evaluate(statement, env)
        
        return lastEvaluated
    elif node.type == "NumericLiteral":
        return runtimevalues.Number(node.value)
    elif node.type == "NullLiteral":
        return runtimevalues.Null()
    elif node.type == "BinaryExpression":
        # due to the nature of python, we dont have to handle operations between booleans and numbers
        lhs = evaluate(node.left, env)
        rhs = evaluate(node.right, env)

        result = 0
        kind = "Number"

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
        elif node.op.type == TokenType.logand:
            return runtimevalues.Boolean(lhs.value and rhs.value)
        elif node.op.type == TokenType.logor:
            return runtimevalues.Boolean(lhs.value or rhs.value)
        elif node.op.type == TokenType.bitand:
            result = lhs.value & rhs.value
        elif node.op.type == TokenType.bitor:
            result = lhs.value | rhs.value
        elif node.op.type == TokenType.bitxor:
            result = lhs.value ^ rhs.value

        return runtimevalues.Number(result)
    elif node.type == "Identifier":
        return env.lookup(node.name)
    elif node.type == "VariableDeclarationStatement":
        if node.init == None:
            init = runtimevalues.Null()
        else:
            init = evaluate(node.init, env)

        env.defineVariable(node.id.name, init, node.kind)

    elif node.type == "BlockStatement":
        blockEnv = enviornment.Enviornment(env)

        for stmt in node.body:
            evaluate(stmt, blockEnv)
    elif node.type == "AssignmentExpression":
        if node.left.type != "Identifier":
            raise error.LynxError(f"Cannot assign to type '{node.left.type}'.", node.pos.line, node.pos.col)
        
        right = evaluate(node.right, env)

        env.assignVar(node.left.name, right)

        return right
    elif node.type == "PrintStatement":
        argument = evaluate(node.argument, env)

        print(stringify(argument))
    else:
        raise error.LynxError(f"Unknown ast node: {node.type}", node.pos.line, node.pos.col)