from team import Team
from league import League
import argparse
import pygame
from pygame.locals import *
import sys


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--simulate",
        action="store_true",
        help="simulates a season outside of a gameloop",
    )
    args = parser.parse_args()

    if args.simulate:

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

    else:
        pygame.init()
        DISPLAYSURF = pygame.display.set_mode((400, 300))
        pygame.display.set_caption('Football Simulator 2022')

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


if __name__ == "__main__":
    main()
