from team import Team
from league import League
import argparse
import time
from enum import Enum
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from states.main_menu_state import MainMenuState


class FootballSimulator:
    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 500
        self.FONT = pygame.font.SysFont("Arial", 20)
        self.FONT_COLOR = pygame.Color('red')
        self.screen = pygame.display.set_mode(
            [self.SCREEN_WIDTH, self.SCREEN_HEIGHT]
        )
        self.S_PER_UPDATE = 0.008
        self.lag = 0
        self.dt, self.prev_time = 0, time.time()
        self.actions = {"mouse_click": False}
        self.game_running = True
        self.state_stack = []
        self.load_states()
        self.player_team = None

    def game_loop(self):
        while self.game_running:
            self.get_dt()
            self.get_events()
            while self.lag >= self.S_PER_UPDATE:
                self.update()
                self.lag -= self.S_PER_UPDATE

            self.render()
            # print(self.state_stack)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # eventually replace to back out of a menu or prompt
                    self.game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions['mouse_click'] = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.actions['mouse_click'] = False

    def update(self):
        self.state_stack[-1].update(self.dt)

    def render(self):
        self.state_stack[-1].render(self.screen)
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now
        self.lag += self.dt

    def load_states(self):
        self.main_menu = MainMenuState(self)
        self.state_stack.append(self.main_menu)


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
        fb = FootballSimulator()
        while fb.game_running:
            fb.game_loop()

        pygame.quit()


if __name__ == "__main__":
    main()
