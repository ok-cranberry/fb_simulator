from team import Team
from league import League
import argparse
import time
from enum import Enum
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT


class MenuButton(pygame.sprite.Sprite):
    def __init__(self, msg: str, position: tuple, fb_simulator):
        super(MenuButton, self).__init__()
        self.x = position[0]
        self.y = position[1]
        self.width = 200
        self.height = 50
        self.fill_color = (255, 255, 255)
        self.msg = msg
        self.position = position

        self.surf = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.fb_simulator = fb_simulator

    def mouse_is_over(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def draw(self, window):
        self.text = self.fb_simulator.FONT.render(
            self.msg, True, self.fb_simulator.FONT_COLOR
        )
        center = (
            (self.width / 2 - self.text.get_width() / 2),
            (self.height / 2 - self.text.get_height() / 2),
        )

        self.surf.fill(self.fill_color)

        if self.mouse_is_over():
            self.surf.fill((0, 255, 0))

        self.surf.blit(self.text, center)
        window.blit(self.surf, self.position)

    def click(self):
        # Probably a future state change action
        # This is a WIP
        if self.fb_simulator.actions["mouse_click"]:
            if self.mouse_is_over():
                print("button click")
                return True
        else:
            return False


class GameState:
    def __init__(self, fb_simulator):
        self.fb_simulator = fb_simulator
        self.prev_state = None

    def update(self, delta_time, actions):
        pass

    def render(self, window):
        pass

    def enter_state(self):
        if len(self.fb_simulator.state_stack) > 1:
            self.prev_state = self.fb_simulator.state_stack[-1]
        self.fb_simulator.state_stack.append(self)

    def exit_state(self):
        self.fb_simulator.state_stack.pop()


class MainMenuState(GameState):
    def __init__(self, fb_simulator):
        GameState.__init__(self, fb_simulator)

        self.start_button = MenuButton("Start!", (100, 300), self.fb_simulator)
        self.quit_button = MenuButton("Quit", (100, 375), self.fb_simulator)

    def update(self, delta_time):

        if self.start_button.click():
            new_state = TeamSelectionState(self.fb_simulator)
            new_state.enter_state()
        if self.quit_button.click():
            self.fb_simulator.game_running = False

    def render(self, window):
        self.start_button.draw(window)
        self.quit_button.draw(window)


class TeamSelectionState(GameState):
    def __init__(self, fb_simulator):
        GameState.__init__(self, fb_simulator)

    def update(self, delta_time):
        pass

    def render(self, window):
        window.fill((0, 0, 0))


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
        self.dt, self.prev_time = 0, 0
        self.actions = {"mouse_click": False}

        self.game_running = True

        self.state_stack = []
        self.load_states()

    def game_loop(self):
        while self.game_running:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()
            print(self.actions['mouse_click'])

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
