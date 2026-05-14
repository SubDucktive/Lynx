import runtimevalues
import error
import enviornment
from Token import TokenType

def truthy(value):
    if value.type == "Null":
        return False
    
    if value.type == "Boolean":
        return value.value
    
    if value.type == "Number":
        return value.value != 0
    
    if value.type == "String":
        return value.value != ""
    
    return True

# will be very useful for later
def stringify(value):
    if value is not None:
        if value.type in ["NumberValue", "NullValue", "StringValue"]:
            return value.value
        elif value.type == "BooleanValue":
            return "true" if value.value else "false"
    return ""

numeric_like = [runtimevalues.types.NumberValue, runtimevalues.types.BooleanValue]

def evaluate(node, env):
    if node.type == "ProgramStatement":
        lastEvaluated = None

        for statement in node.statements:
            lastEvaluated = evaluate(statement, env)
        
        return lastEvaluated
    elif node.type == "NumericLiteral":
        return runtimevalues.Number(node.value)
    elif node.type == "StringLiteral":
        return runtimevalues.String(node.value)
    elif node.type == "NullLiteral":
        return runtimevalues.Null()
    elif node.type == "BinaryExpression":
        lhs = evaluate(node.left, env)
        rhs = evaluate(node.right, env)

        if lhs.type in numeric_like and rhs.type in numeric_like:
            if node.op.type == TokenType.plus:
                result = lhs.value + rhs.value
            elif node.op.type == TokenType.minus:
                result = lhs.value - rhs.value
            elif node.op.type == TokenType.mult:
                result = lhs.value * rhs.value
            elif node.op.type == TokenType.divide:
                if rhs.value == 0:
                    raise error.LynxError("Cannot divide by zero", node.left.pos.line, node.left.pos.col)
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
            elif node.op.type == TokenType.equalto:
                return runtimevalues.Boolean(lhs.value == rhs.value)
            elif node.op.type == TokenType.notequal:
                return runtimevalues.Boolean(lhs.value != rhs.value)
            elif node.op.type == TokenType.lessthan:
                return runtimevalues.Boolean(lhs.value < rhs.value)
            elif node.op.type == TokenType.lessequal:
                return runtimevalues.Boolean(lhs.value <= rhs.value)
            elif node.op.type == TokenType.greaterthan:
                return runtimevalues.Boolean(lhs.value > rhs.value)
            elif node.op.type == TokenType.greaterequal:
                return runtimevalues.Boolean(lhs.value >= rhs.value)


            return runtimevalues.Number(result)
        elif lhs.type == rhs.type == runtimevalues.types.StringValue:
            if node.op.type == TokenType.plus:
                return runtimevalues.String(lhs.value + rhs.value)
            else:
                raise error.LynxError (
                    "Invalid operator for string operations.",
                    node.left.pos.line, node.left.pos.col
                )
        else:
            raise error.LynxError (
                f"Cannot do operations on type '{lhs.type}' and '{rhs.type}'",
                node.left.pos.line, node.left.pos.col
            )
    

    elif node.type == "UnaryExpression":
        arg = evaluate(node.arg, env)

        result = 0

        if node.op.type == TokenType.minus:
            return runtimevalues.Number(arg.value * -1)
        elif node.op.type == TokenType.lognot:
            return runtimevalues.Boolean(not truthy(arg))

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
    elif node.type == "IfStatement":
        if truthy(evaluate(node.test, env)):
            evaluate(node.consequent, env)
        elif node.alternate is not None:
            evaluate(node.alternate, env)
    else:
        raise error.LynxError(f"Unknown ast node: {node.type}", node.pos.line, node.pos.col)