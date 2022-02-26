import positions
from player_database import db


class Team:
    def __init__(self, name):
        self.name = name

        if self.name in db:
            self.quarterback = positions.Quarterback(db[self.name]["QB"])
            self.wide_receiver = positions.WideReceiver(db[self.name]["WR"])
            self.defensive_back = positions.DefensiveBack(db[self.name]["DB"])
        else:
            self.quarterback = positions.Quarterback("QB #10")
            self.wide_receiver = positions.WideReceiver("WR #81")
            self.defensive_back = positions.DefensiveBack("DB # 25")
