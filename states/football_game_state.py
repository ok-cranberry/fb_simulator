from game import Game
from menu_button import MenuButton
from states.game_state import GameState
from states.game_end_state import GameEndState
from team import Team
from play import Play
from clock import GameClock
from announcer import Announcer
import time


class FootballGameState(GameState):
    def __init__(self, fb_simulator):
        GameState.__init__(self, fb_simulator)

        # TODO: Remove hardcoded team matchup
        self.fb_simulator.other_team = Team("Geibel")
        # TODO: properly place temporary GameClock

        self.announcer = Announcer()

        self.game = Game(
            self.fb_simulator.player_team,
            self.fb_simulator.other_team,
            self.announcer,
        )
        self.game.start_game()

        self.game_matchup_banner = MenuButton(
            f"{self.fb_simulator.player_team.name} v { self.fb_simulator.other_team.name}",
            (100, 100),
            self.fb_simulator,
        )
        self.game_score_banner = MenuButton(
            f"{self.game.score[self.game.home_team]} - {self.game.score[self.game.away_team]}",
            (100, 150),
            self.fb_simulator,
        )

        self.game_log_banner = MenuButton(
            "-",
            (0, 200),
            self.fb_simulator,
            width=500,
        )

        self.game_clock_banner = MenuButton(
            self.game.clock.format_clock(),
            (150, 250),
            self.fb_simulator,
        )

        self.game_quarter_banner = MenuButton(
            f"Q{self.game.quarter}",
            (150, 300),
            self.fb_simulator,
        )

    def update(self, delta_time):
        # self.game.clock.clock_countdown()

        self.game_matchup_banner = MenuButton(
            f"{self.fb_simulator.player_team.name} v { self.fb_simulator.other_team.name}",
            (100, 100),
            self.fb_simulator,
        )
        self.game_score_banner = MenuButton(
            f"{self.game.score[self.game.home_team]} - {self.game.score[self.game.away_team]}",
            (100, 150),
            self.fb_simulator,
        )

        self.game_log_banner = MenuButton(
            self.announcer.return_commentary(),
            (0, 200),
            self.fb_simulator,
            width=500,
        )

        self.game_clock_banner = MenuButton(
            self.game.clock.format_clock(),
            (150, 250),
            self.fb_simulator,
        )

        self.game_quarter_banner = MenuButton(
            f"Q{self.game.quarter}",
            (150, 300),
            self.fb_simulator,
        )

        if self.game_matchup_banner.click():
            self.game.continue_game()
        # time.sleep(1)
        if self.game.end_of_game is True:
            new_state = GameEndState(self.fb_simulator)
            new_state.enter_state()

    def render(self, window):
        window.fill((0, 0, 0))
        self.game_matchup_banner.draw(window)
        self.game_score_banner.draw(window)
        self.game_log_banner.draw(window)
        self.game_clock_banner.draw(window)
        self.game_quarter_banner.draw(window)
