from error import LynxError

class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Enviornment:
    def __init__(self, parent=None):
        self.variables = []
        self.parent = parent

    def defineBuiltinVar(self, name, value):
        self.variables.append(Variable(name, value))

    def defineVariable(self, name, value):
        if self.varExists(name):
            raise LynxError(f"Cannot declare variable '{name.value}, it already exists in this scope'", name.pos.line, name.pos.col)
        
        self.variables.append(Variable(name.value, value))

    def varExists(self, name):
        for variable in self.variables:
            if variable.name == name.value:
                return True
        return False

    def resolve(self, name):
        # name argument is a token passed in

        if self.varExists(name):
            return self
        
        if self.parent == None:
            raise LynxError(f"Couldn't resolve variable: '{name.value}'", name.pos.line, name.pos.col)
        
        return self.parent.resolve(name)
    
    def lookup(self, name):
        env = self.resolve(name)

        index = [index for index, variable in enumerate(env.variables) if variable.name == name.value][0]
        
        return env.variables[index].value




        

