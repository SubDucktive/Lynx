class Number:
    def __init__(self, value):
        self.type = "NumberValue"
        self.value = value

class Null:
    def __init__(self):
        self.type = "NullValue"

        self.value = "null"