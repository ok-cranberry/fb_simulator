import positions


class Team:
    def __init__(self, name):
        self.name = name

        self.quarterback = positions.Quarterback("Charlie Manack")
        self.wide_receiver = positions.WideReceiver("Hunter Patterson")
        self.defensive_back = positions.DefensiveBack("Chris Pierce")
