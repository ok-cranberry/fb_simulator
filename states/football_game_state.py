from game import Game
from menu_button import MenuButton
from states.game_state import GameState
from team import Team
from play import Play
from clock import GameClock
from announcer import Announcer


class FootballGameState(GameState):
    def __init__(self, fb_simulator):
        GameState.__init__(self, fb_simulator)

        # TODO: Remove hardcoded team matchup
        self.fb_simulator.other_team = Team("Geibel")
        # TODO: properly place temporary GameClock
        self.clock = GameClock()

        self.announcer = Announcer()

        # self.game = Game(self.fb_simulator.player_team, self.fb_simulator.other_team)
        # self.game.game()
        self.play = Play(
            20,
            self.fb_simulator.player_team,
            self.fb_simulator.other_team,
            self.clock,
            self.announcer,
        )
        self.play.start_play()

        # self.game_matchup_banner = MenuButton(
        #     f"{self.fb_simulator.player_team.name} v { self.fb_simulator.other_team.name}",
        #     (100, 100),
        #     self.fb_simulator,
        # )
        # self.game_score_banner = MenuButton(
        #     f"{self.game.score[self.game.home_team]} - {self.game.score[self.game.away_team]}",
        #     (100, 150),
        #     self.fb_simulator,
        # )
        self.game_log_banner = MenuButton(
            self.announcer.return_commentary(),
            (0, 200),
            self.fb_simulator,
            width=500,
        )

    def update(self, delta_time):
        pass

    def render(self, window):
        window.fill((0, 0, 0))
        # self.game_matchup_banner.draw(window)
        # self.game_score_banner.draw(window)
        self.game_log_banner.draw(window)
