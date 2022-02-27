from game import Game

class Season:
    def __init__(self, schedule):

        self.schedule = schedule

        self.standings = {}

    def modify_standings(self, matchup, winner):

        for team in matchup:
            if team not in self.standings:
                self.standings[team] = [0,0,0]

            if team == winner:
                self.standings[team][0] += 1
            else:
                if winner is None:
                    self.standings[team][2] += 1
                else:
                    self.standings[team][1] += 1


    def play_season(self):

        for week in self.schedule:
            for matchup in week:
                home_team = matchup[0]
                away_team = matchup[1]

                game = Game(home_team, away_team)
                game.game()

                self.modify_standings(matchup, game.winner)
                # if game.winner in self.standings:
                #     self.standings[game.winner] += 1
                # else:
                #     if game.winner is None:
                #         pass
                #     else:
                #         self.standings[game.winner] = 1

    # season standings

    # crown season champion
