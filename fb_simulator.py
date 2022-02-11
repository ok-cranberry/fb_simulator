from team import Team
from game import Game


def main():

    home_team = Team("Frazier")
    away_team = Team("Geibel")

    game = Game(home_team, away_team)
    game.game()


if __name__ == "__main__":
    main()
