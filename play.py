import offense
import random
from team import Team
from clock import GameClock
from announcer import Announcer


class Play:
    def __init__(
        self,
        line_of_scrimmage,
        offense,
        defense,
        clock: GameClock,
        announcer: Announcer,
    ):
        self.line_of_scrimmage = line_of_scrimmage
        self.offense = offense
        self.defense = defense
        self.clock = clock
        self.announcer = announcer

        yards_gained = 0

    def presnap(self):
        """TODO: Add functionality for the teams to apply some weight to the ensuing play"""

        self.announcer.store_commentary(
            f"{self.offense.quarterback.name} brings his team up to the line"
        )
        print(
            f"{self.offense.quarterback.name} brings his team up to the line"
        )
        print(self.clock.format_clock())
        self.clock.intra_play_duration(30)

    def action(self):

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
        self.presnap()
        if not self.clock.get_current_time() <= 0:
            return self.action()
        else:
            print("Oh they couldn't get the play off in time")
            return (0, False)
