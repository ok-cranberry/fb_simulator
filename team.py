import positions
from player_database import db


class Team:
    def __init__(self, name):
        self.name = name

        if self.name in db:
            self.quarterback = positions.Quarterback(db[self.name]["QB"])
            self.running_back = positions.RunningBack(db[self.name]["RB"])
            self.wide_receiver = positions.WideReceiver(db[self.name]["WR"])
            self.linebacker = positions.Linebacker(db[self.name]["LB"])
            self.defensive_back = positions.DefensiveBack(db[self.name]["DB"])
        else:
            self.quarterback = positions.Quarterback("QB #10")
            self.running_back = positions.RunningBack("RB #22")
            self.wide_receiver = positions.WideReceiver("WR #81")
            self.linebacker = positions.Linebacker("LB #55")
            self.defensive_back = positions.DefensiveBack("DB #25")

        self.roster = {
            "QB": self.quarterback,
            "RB": self.running_back,
            "WR": self.wide_receiver,
            "LB": self.linebacker,
            "DB": self.defensive_back,
        }
