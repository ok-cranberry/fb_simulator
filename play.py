import random

class Quarterback:
    def __init__(self, name):
        self.name = name
        setattr(self, "accuracy", random.randrange(1,20))

class WideReciever:
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


def presnap():
    pass

def action(quarterback, wide_receiver, defensive_back):
    print("It's a pass!")

    outcome = weights(0.6) * quarterback.accuracy + weights(0.4) * wide_receiver.catching - weights(0.5) * defensive_back.coverage
    print(outcome)


def result():
    pass

def main():

    QB = Quarterback("Charlie Manack")
    WR = WideReciever("Hunter Patterson")
    DB = DefensiveBack("Chris Pierce")

    # print(QB.accuracy)
    # print(WR.catching)
    # print(DB.coverage)

    presnap()
    action(QB, WR, DB)
    result()

if __name__ == "__main__":
    main()
