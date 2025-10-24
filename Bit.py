class Bit:
    state: bool

    def __init__(self, bit: bool | int):
        self.state = bit if type(bit) is bool else bool(bit)

    def __str__(self):
        return '1' if self else '0'

    def __and__(self, other):
        return Bit(1) if self == other else Bit(0)

    def __not__(self):
        return Bit(0) if self else Bit(1)

    def __eq__(self, other):
        return Bit(1) if self == other else Bit(0)

    def __bool__(self):
        return self.state
