import random


class Quarterback:
    def __init__(self, name):
        self.name = name
        setattr(self, "accuracy", random.randrange(1, 20))


class WideReceiver:
    def __init__(self, name):
        self.name = name
        setattr(self, "catching", random.randrange(1, 20))


class DefensiveBack:
    def __init__(self, name):
        self.name = name
        setattr(self, "coverage", random.randrange(1, 20))
