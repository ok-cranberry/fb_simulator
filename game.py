import drive
from team import Team
import clock


class Game:
    def __init__(self, home_team, away_team):
        """for now, this will be 3 drives per half for each team, no kickoffs"""
        self.home_team = home_team
        self.away_team = away_team

        self.home_score = 0
        self.away_score = 0
        self.home_yardage = 0
        self.away_yardage = 0
        self.clock = clock.GameClock()
        self.quarter = 1

    def coin_toss(self):
        pass

    def find_starting_yardline(self, drive: drive.Drive):
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
        elif away_score > home_score:
            print(
                f"And that's your Final, with {self.away_team.name} winning {away_score} to {home_score}"
            )
        else:
            print(
                f"Wow, what an even game! That's it for us here, with {self.away_team.name} and {self.home_team.name} ending in a tied game, knotted up at {home_score} "
            )

    def print_score(self):
        """Prints the score based on the result of a Drive

        drive - Drive object type
        """
        print(
            f"{self.away_team.name}: {self.away_score} - {self.home_team.name}: {self.home_score}"
        )

    def game(self):

        print(self.clock.get_current_time())

        self.coin_toss()

        # game's/half's starting yardline
        yardline = 20

        while self.quarter <= 4:

            while self.clock.get_current_time() < 0:
                away_team_drive = drive.Drive(
                    yardline, self.away_team, self.home_team
                )
                away_team_drive.drive()

                self.away_score += away_team_drive.score
                self.print_score()

                self.away_yardage += away_team_drive.drive_yardage

                yardline = self.find_starting_yardline(away_team_drive)

                # home team drive
                home_team_drive = drive.Drive(
                    yardline, self.home_team, self.away_team
                )
                home_team_drive.drive()

                self.home_score += home_team_drive.score
                self.print_score()

                self.home_yardage += home_team_drive.drive_yardage

                yardline = self.find_starting_yardline(home_team_drive)

            self.quarter += 1

        # declare winner
        self.final_score(
            self.home_score,
            self.away_score,
        )
