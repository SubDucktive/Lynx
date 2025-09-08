from position import Position

class LynxError(Exception):
    def __init__(self, message, line=None, column=None):
        super().__init__(message)
        self.message = message
        
        self.pos = Position(line, column)

    def __str__(self):
        if self.line is None and self.column is None:
            return f"Error: {self.message}"
        
        return f"Error at {self.pos.line}:{self.pos.col} : {self.message}"