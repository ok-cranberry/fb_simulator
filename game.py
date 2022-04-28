from drive import Drive
from team import Team
import clock
import random


class Game:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

        self.score = {self.home_team: 0, self.away_team: 0}
        self.yardage = {self.home_team: 0, self.away_team: 0}
        self.home_team.possessions = 0
        self.clock = clock.GameClock()
        self.quarter = 1
        self.opening_possession = ()
        self.winner = None
        self.loser = None

    def coin_toss(self):
        flip = random.randint(0, 1)
        if flip == 0:
            # away team gets first possessions
            self.opening_possession = (self.away_team, self.home_team)
        else:
            self.opening_possession = (self.home_team, self.away_team)

    def find_starting_yardline(self, drive: Drive):
        if drive.current_yardline < 100:
            # if the team did not score TD
            return drive.current_yardline
        else:
            return 20

    def final_score(
        self,
        home_score: int,
        away_score: int,
    ):
        if home_score > away_score:
            print(
                f"And that's your Final, with {self.home_team.name} winning {home_score} to {away_score}"
            )
            self.winner = self.home_team
            self.loser = self.away_team

        elif away_score > home_score:
            print(
                f"And that's your Final, with {self.away_team.name} winning {away_score} to {home_score}"
            )
            self.winner = self.away_team
            self.loser = self.home_team
        else:
            print(
                f"Wow, what an even game! That's it for us here, with {self.away_team.name} and {self.home_team.name} ending in a tied game, knotted up at {home_score} "
            )

    def print_score(self):
        """Prints the score based on the result of a Drive

        drive - Drive object type
        """
        print(
            f"{self.away_team.name}: {self.score[self.away_team]} - {self.home_team.name}: {self.score[self.home_team]}"
        )

    def new_possesion(self, yardline, offense: Team, defense: Team):
        team_drive = Drive(yardline, offense, defense, self.clock)
        team_drive.drive()

        self.score[offense] += team_drive.score
        self.print_score()

        self.yardage[offense] += team_drive.drive_yardage

        # yardline = self.find_starting_yardline(team_drive)

    def game(self):

        print(self.clock.get_current_time())
        print(self.home_team.possessions)

        self.coin_toss()

        # game's/half's starting yardline
        yardline = 20

        while self.quarter <= 4:
            # run alternating possessions for home and away teams
            while self.clock.get_current_time() > 0:

                self.new_possesion(yardline, self.away_team, self.home_team)
                self.new_possesion(yardline, self.home_team, self.away_team)

            print(f"We've reached the end of the {self.quarter} quarter")
            self.print_score
            self.quarter += 1
            self.clock.reset_clock_for_quarter()

        # declare winner
        self.final_score(
            self.score[self.home_team],
            self.score[self.away_team],
        )

    def start_game(self):
        # Coin toss
        self.coin_toss()

        # initialize the first drive
        self.current_drive = Drive(
            20,
            self.opening_possession[0],
            self.opening_possession[1],
            self.clock,
        )

        # Starting Flavor Text "Blah will receive the ball first"
        print("Start Game")

    def continue_game(self):

        print(self.clock.get_current_time())

        if self.quarter <= 4:
            if self.clock.get_current_time() > 0:
                # next play
                # maybe stash this in the Drive as continue_drive, and have the logic there
                self.current_drive.continue_drive()
                # check if change of possesion
                if self.current_drive.end_of_drive is True:

                    self.score[
                        self.current_drive.offense
                    ] += self.current_drive.score
                    self.print_score()

                    self.yardage[
                        self.current_drive.offense
                    ] += self.current_drive.drive_yardage

                    starting_yardline = self.find_starting_yardline(
                        self.current_drive
                    )

                    self.prev_drive = self.current_drive
                    self.current_drive = Drive(
                        starting_yardline,
                        self.prev_drive.defense,
                        self.prev_drive.offense,
                        self.clock,
                    )
            else:
                self.quarter += 1
                self.clock.reset_clock_for_quarter()
                if self.quarter == 3:
                    pass
                    # announer annouces halftime
        else:
            pass
            # end of game
            # post game displays
