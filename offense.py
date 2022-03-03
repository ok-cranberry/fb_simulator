import random
from clock import GameClock
from team import Team


def weights(nominal_weight):
    """Adds a random fudge factor to a play contribution weights
    nominal_weight : float - between 0-1
    """

    return nominal_weight * random.gauss(0.5, 1 / 3)

def play_outcomes():
    # determines the play outcome by averaging the results of 100 instances

    i = 0
    play_outcomes = []
    while i < 100:
        outcome = (
            # weights(0.6) * offense.quarterback.accuracy
            # + weights(0.4) * offense.wide_receiver.catching
            # - weights(0.5) * defense.defensive_back.coverage
        )
        play_outcomes.append(outcome)
        i += 1

    return sum(play_outcomes) / len(play_outcomes)

def pass_play(offense: Team, defense: Team, clock: GameClock):
    # basic pass play by the Offense

    turnover = False
    yards_gained = 0

    print("It's a pass!")
    i = 0
    play_outcomes = []
    while i < 100:
        outcome = (
            weights(0.6) * offense.quarterback.accuracy
            + weights(0.4) * offense.wide_receiver.catching
            - weights(0.5) * defense.defensive_back.coverage
        )
        play_outcomes.append(outcome)
        i += 1

    avg_outcome = sum(play_outcomes) / len(play_outcomes)

    if avg_outcome > 1:
        print(f"It's caught by {offense.wide_receiver.name}!!")
        yards_gained = int(avg_outcome * 5)
        # will need to modify to take a distribution into account or to change the weights
        print(f"That's a gain of {yards_gained}")

        # update stats
        offense.quarterback.passing_yards += yards_gained
        offense.quarterback.completions += 1
        offense.quarterback.passing_attempts += 1
        offense.wide_receiver.receptions += 1
        offense.wide_receiver.receiving_yards += yards_gained

        clock.play_duration(12)
    elif avg_outcome <= -1:
        print(
            f"{offense.quarterback.name} is intercepted by {defense.defensive_back.name}!!"
        )
        clock.play_duration(12)
        turnover = True
        # Function for Return Yards

        # update stats
        offense.quarterback.passing_attempts += 1
        defense.defensive_back.interceptions += 1

    elif avg_outcome > -1 and avg_outcome <= 1:
        print(f"It's incomplete!")
        yards_gained = 0
        clock.play_duration(8)

        # update stats
        offense.quarterback.passing_attempts += 1

    return yards_gained, turnover


def running_play(offense: Team, defense: Team, clock: GameClock):
    # basic running play by the Offense

    turnover = False
    yards_gained = 0

    print(f"{offense.quarterback.name} hands the ball off to {offense.running_back.name}!")
    i = 0
    play_outcomes = []
    while i < 100:
        outcome = (
            weights(0.5) * offense.running_back.speed
            - weights(0.5) * defense.linebacker.tackling
        )
        play_outcomes.append(outcome)
        i += 1

    avg_outcome = sum(play_outcomes) / len(play_outcomes)


    print(f"{offense.running_back.name} takes it off tackle..")
    yards_gained = int(avg_outcome * 3)
    # will need to modify to take a distribution into account or to change the weights
    if yards_gained >0:
        print(f"That's a gain of {yards_gained}")
    elif yards_gained is 0:
        print(f"He'stopped at the line by {defense.linebacker.name}")
    else:
        print(f"Wow that's a loss of {-1*yards_gained} on the play!")

    offense.running_back.rushing_yards += yards_gained

    return yards_gained, turnover
