import drive


class Game:
    def __init__(self, home_team, away_team):
        """for now, this will be 3 drives per half for each team, no kickoffs"""
        self.home_team = home_team
        self.away_team = away_team

        self.home_score = 0
        self.away_score = 0

    def game(self):

        away_team_drive = drive.Drive(
            20,
            self.away_team.quarterback,
            self.away_team.wide_receiver,
            self.away_team.defensive_back,
        )
        away_team_drive.drive()
        self.away_score += away_team_drive.score
        print(
            f"{self.away_team.name}: {self.away_score} - {self.home_team.name}: {self.home_score}"
        )

        home_team_drive = drive.Drive(
            20,
            self.home_team.quarterback,
            self.home_team.wide_receiver,
            self.home_team.defensive_back,
        )
        home_team_drive.drive()
        self.home_score += home_team_drive.score
        print(
            f"{self.away_team.name}: {self.away_score} - {self.home_team.name}: {self.home_score}"
        )

    # establish home and away teams
    # track drives for each
    # track yardage for each
    # track score for each teams
    # declare a winner
