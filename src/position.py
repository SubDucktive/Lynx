class Position:
    def __init__(self, line, col):
        self.line = line
        self.col = col

    def dict(self):
        return {
            "line": self.line,
            "col": self.col
        }