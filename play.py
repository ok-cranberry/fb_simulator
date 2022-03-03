import offense
import random
from team import Team
from clock import GameClock


class Play:
    def __init__(self, line_of_scrimmage, offense, defense, clock: GameClock):
        self.line_of_scrimmage = line_of_scrimmage
        self.offense = offense
        self.defense = defense
        self.clock = clock

        yards_gained = 0

    def presnap(self, quarterback):
        """TODO: Add functionality for the teams to apply some weight to the ensuing play"""

        print(f"{quarterback.name} brings his team up to the line")
        print(self.clock.format_clock())
        self.clock.intra_play_duration(30)

    def action(self, quarterback, wide_receiver, defensive_back):

        playcall = random.randint(1, 2)
        if playcall == 1:
            yards_gained, turnover = offense.pass_play(
                self.offense, self.defense, self.clock
            )
        else:
            yards_gained, turnover = offense.running_play(
                self.offense, self.defense, self.clock
            )

        return yards_gained, turnover

    def start_play(self):
        self.presnap(self.offense.quarterback)
        if not self.clock.get_current_time() <= 0:
            return self.action(
                self.offense.quarterback,
                self.offense.wide_receiver,
                self.defense.defensive_back,
            )
        else:
            print("Oh they couldn't get the play off in time")
            return (0, False)
