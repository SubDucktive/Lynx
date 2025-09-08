from error import LynxError

class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Enviornment:
    def __init__(self, parent=None):
        self.variables = []
        self.parent = parent

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
            raise LynxError(f"Couldn't resolve variable: '{name.value}'")
        
        return self.parent.resolve(name)
    
    def lookup(self, name):
        env = self.resolve(name.value)

        index = [index for index, variable in enumerate(env.variables) if variable.name == name.value][0]
        
        return env.variables[index].value




        

