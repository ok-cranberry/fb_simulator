import random

def weights(nominal_weight):
    """Adds a random fudge factor to a play contribution weights
    nominal_weight : float - between 0-1
    """

    return nominal_weight * random.gauss(0.5, 1 / 3)

class PlayFromScrimmage:
    def __init__(self, line_of_scrimmage, quarterback, wide_receiver, defensive_back):
        self.line_of_scrimmage = line_of_scrimmage
        self.quarterback = quarterback
        self.wide_receiver = wide_receiver
        self.defensive_back = defensive_back

        yards_gained = 0

    def presnap(self,quarterback, wide_receiver, defensive_back):
        """TODO: Add functionality for the teams to apply some weight to the ensuing play"""

        print(f"{quarterback.name} brings his team up to the line")

    def action(self,quarterback, wide_receiver, defensive_back):

        # turnover = False
        yards_gained = 0

        print("It's a pass!")
        i = 0
        play_outcomes = []
        while i < 100:
            outcome = (
                weights(0.6) * quarterback.accuracy
                + weights(0.4) * wide_receiver.catching
                - weights(0.5) * defensive_back.coverage
            )
            play_outcomes.append(outcome)
            i += 1

        avg_outcome = sum(play_outcomes) / len(play_outcomes)

        if avg_outcome > 1:
            print(f"It's caught by {wide_receiver.name}!!")
            yards_gained = int(avg_outcome * 5)
            # will need to modify to take a distribution into account or to change the weights
            print(f"That's a gain of {yards_gained}")
        elif avg_outcome <= -1:
            print(f"{quarterback.name} is intercepted by {defensive_back.name}!!")
            # turnover = True
            # Function for Return Yards
        elif avg_outcome > -1 and avg_outcome <= 1:
            print(f"It's incomplete!")

        return yards_gained

    def result(self, line_of_scrimmage, yards_gained):
        """Update the down, distance, and score"""
        line_of_scrimmage += yards_gained
        if line_of_scrimmage >= 100:
            print("TOUCHDOWN!!")


    def play(self):
        self.presnap(self.quarterback, self.wide_receiver, self.defensive_back)
        yards_gained = self.action(self.quarterback, self.wide_receiver, self.defensive_back)
        self.result(self.line_of_scrimmage, yards_gained)
