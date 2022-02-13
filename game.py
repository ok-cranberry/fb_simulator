import drive
from team import Team


class Game:
    def __init__(self, home_team, away_team):
        """for now, this will be 3 drives per half for each team, no kickoffs"""
        self.home_team = home_team
        self.away_team = away_team

        self.home_score = 0
        self.away_score = 0

    def final_score(
        self,
        home_score: int,
        away_score: int,
        home_team: Team,
        away_team: Team,
    ):
        if home_score > away_score:
            print(
                f"And that's your Final, with {home_team.name} winning {home_score} to {away_score}"
            )
        elif away_score > home_score:
            print(
                f"And that's your Final, with {away_team.name} winning {away_score} to {home_score}"
            )
        else:
            print(
                f"Wow, what an even game! That's it for us here, with {away_team.name} and {home_team.name} ending in a tied game, knotted up at {home_score} "
            )

    def game(self):

        # TODO coin toss

        for i in range(6):
            away_team_drive = drive.Drive(
                20,
                self.away_team,
            )
            away_team_drive.drive()
            self.away_score += away_team_drive.score
            print(
                f"{self.away_team.name}: {self.away_score} - {self.home_team.name}: {self.home_score}"
            )

            home_team_drive = drive.Drive(
                20,
                self.home_team,
            )
            home_team_drive.drive()
            self.home_score += home_team_drive.score
            print(
                f"{self.away_team.name}: {self.away_score} - {self.home_team.name}: {self.home_score}"
            )

        # declare winner
        self.final_score(
            self.home_score,
            self.away_score,
            self.home_team,
            self.away_team,
        )

    # establish home and away teams
    # track drives for each
    # track yardage for each
    # track score for each teams
    # declare a winner
