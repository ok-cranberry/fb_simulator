import random


class Player:
    def __init__(self, name):
        self.name = name
        self.passing_yards = 0
        self.completions = 0
        self.passing_attempts = 0
        self.passing_touchdowns = 0
        self.receptions = 0
        self.receiving_yards = 0
        self.interceptions = 0


class Quarterback(Player):
    def __init__(self, name):
        super().__init__(name)
        setattr(self, "accuracy", random.randrange(1, 20))


class WideReceiver(Player):
    def __init__(self, name):
        super().__init__(name)
        setattr(self, "catching", random.randrange(1, 20))


class DefensiveBack(Player):
    def __init__(self, name):
        super().__init__(name)
        setattr(self, "coverage", random.randrange(1, 20))
