import random

class Quarterback:
    def __init__(self, name):
        self.name = name
        setattr(self, "accuracy", random.randrange(1,20))

class WideReceiver:
    def __init__(self, name):
        self.name = name
        setattr(self, "catching", random.randrange(1,20))

class DefensiveBack:
    def __init__(self, name):
        self.name = name
        setattr(self, "coverage", random.randrange(1,20))

def weights(nominal_weight):
    """ Adds a random fudge factor to a play contribution weights
    nominal_weight : float - between 0-1
    """

    return nominal_weight * random.gauss(0.5, 1/3)


def presnap(quarterback, wide_receiver, defensive_back):
    """TODO: Add functionality for the teams to apply some weight to the ensuing play"""

    print(f"{quarterback.name} brings his team up to the line")

def action(quarterback, wide_receiver, defensive_back):
    print("It's a pass!")
    i = 0
    play_outcomes = []
    while i<100:
        outcome = weights(0.6) * quarterback.accuracy + weights(0.4) * wide_receiver.catching - weights(0.5) * defensive_back.coverage
        play_outcomes.append(outcome)
        i += 1

    avg_outcome = sum(play_outcomes)/len(play_outcomes)

    if avg_outcome > 1:
        print(f"It's caught by {wide_receiver.name}!!")
    elif avg_outcome <= -1:
        print(f"{quarterback.name} is intercepted by {defensive_back.name}!!")
    elif avg_outcome > -1 and avg_outcome <= 1:
        print(f"It's incomplete!")


def result(quarterback, wide_receiver, defensive_back):
    """Update the down, distance, and score"""
    pass

def main():

    QB = Quarterback("Charlie Manack")
    WR = WideReceiver("Hunter Patterson")
    DB = DefensiveBack("Chris Pierce")

    presnap(QB, WR, DB)
    action(QB, WR, DB)
    result(QB, WR, DB)

if __name__ == "__main__":
    main()
