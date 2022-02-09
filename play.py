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



def presnap():
    pass

def action():
    pass

def result():
    pass

def main():

    QB = Quarterback("Charlie Manack")
    WR = WideReciever("Hunter Patterson")
    DB = DefensiveBack("Chris Pierce")

    print(QB.accuracy)
    print(WR.catching)
    print(DB.coverage)

    presnap()
    action()
    result()

if __name__ == "__main__":
    main()
