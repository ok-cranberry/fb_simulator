import positions
from player_database import db


class Team:
    def __init__(self, name):
        self.name = name

        self.quarterback = positions.Quarterback(db[self.name]["QB"])
        self.wide_receiver = positions.WideReceiver(db[self.name]["WR"])
        self.defensive_back = positions.DefensiveBack(db[self.name]["DB"])
