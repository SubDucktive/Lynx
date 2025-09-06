class LynxError(Exception):
    def __init__(self, message, line, column):
        super().__init__(message)
        self.message = message
        self.line = line
        self.column = column

    def __str__(self):
        return f"Error at {self.line}:{self.column} : {self.message}"