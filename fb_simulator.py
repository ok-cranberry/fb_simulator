from team import Team
from game import Game
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


if __name__ == "__main__":
    main()
