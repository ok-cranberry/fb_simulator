from team import Team
from league import League


def main():

    conference = League(
        (
            Team("Frazier"),
            Team("Geibel"),
            Team("Monessen"),
            Team("West Greene"),
        )
    )

    conference.start_season()
    conference.season_stats()


if __name__ == "__main__":
    main()
