from season import Season


class League:
    def __init__(self, teams):
        self.teams = teams

    def schedule_league_season(self):

        week_1 = [
            (self.teams[0], self.teams[1]),
            (self.teams[2], self.teams[3]),
        ]
        week_2 = [
            (self.teams[0], self.teams[2]),
            (self.teams[3], self.teams[1]),
        ]
        week_3 = [
            (self.teams[0], self.teams[3]),
            (self.teams[1], self.teams[2]),
        ]

        return (week_1, week_2, week_3)

    def start_season(self):

        schedule = self.schedule_league_season()

        season = Season(schedule)
        season.play_season()

        for team in season.standings:
            print(
                f"{team.name:<10}\t {season.standings[team][0]}-{season.standings[team][1]}-{season.standings[team][2]}"
            )

    def season_stats(self):

        league_quarterbacks = []
        league_wide_receivers = []
        league_defensive_backs = []
        league_running_backs = []

        for team in self.teams:
            league_quarterbacks.append(
                {
                    team.quarterback.name: {
                        "passing_yards": team.quarterback.passing_yards,
                        "completions": team.quarterback.completions,
                        "passing_attempts": team.quarterback.passing_attempts,
                    }
                }
            )

            league_wide_receivers.append(
                {
                    team.wide_receiver.name: {
                        "receptions": team.wide_receiver.receptions,
                        "receiving_yards": team.wide_receiver.receiving_yards,
                    }
                }
            )

            league_defensive_backs.append(
                {
                    team.defensive_back.name: {
                        "interceptions": team.defensive_back.interceptions,
                    }
                }
            )
            league_running_backs.append(
                {
                    team.running_back.name: {
                        "rushing_yards": team.running_back.rushing_yards,
                    }
                }
            )

        for qb in league_quarterbacks:
            print(qb)

        for rb in league_running_backs:
            print(rb)
