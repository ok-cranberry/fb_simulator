from season import Season

class League:
    def __init__(self, teams):
        self.teams = teams



    def schedule_league_season(self):

        week_1 = [(self.teams[0], self.teams[1]),(self.teams[2], self.teams[3])]
        week_2 = [(self.teams[0], self.teams[2]),(self.teams[3], self.teams[1])]
        week_3 = [(self.teams[0], self.teams[3]),(self.teams[1], self.teams[2])]

        return (week_1, week_2, week_3)


    def start_season(self):

        schedule = self.schedule_league_season()

        season = Season(schedule)
        season.play_season()

        for team in season.standings:
            print(f"{team.name:<10}\t {season.standings[team][0]}-{season.standings[team][1]}-{season.standings[team][2]}")
