from menu_button import MenuButton
from states.football_game_state import FootballGameState
from states.game_state import GameState


class TeamOverviewState(GameState):
    def __init__(self, fb_simulator):
        GameState.__init__(self, fb_simulator)

        self.team_name_banner = MenuButton(
            self.fb_simulator.player_team.name, (0, 0), self.fb_simulator
        )
        self.roster_banner = MenuButton("Roster", (0, 100), self.fb_simulator)

        self.quarterback_button = MenuButton(
            "QB: " + self.fb_simulator.player_team.quarterback.name,
            (0, 150),
            self.fb_simulator,
        )
        self.running_back_button = MenuButton(
            "RB: " + self.fb_simulator.player_team.running_back.name,
            (0, 200),
            self.fb_simulator,
        )
        self.wide_receiver_button = MenuButton(
            "WR: " + self.fb_simulator.player_team.wide_receiver.name,
            (0, 250),
            self.fb_simulator,
        )
        self.linebacker_button = MenuButton(
            "LB: " + self.fb_simulator.player_team.linebacker.name,
            (0, 300),
            self.fb_simulator,
        )
        self.defensive_back_button = MenuButton(
            "DB: " + self.fb_simulator.player_team.defensive_back.name,
            (0, 350),
            self.fb_simulator,
        )

        self.next_game_banner = MenuButton(
            "Next Game:",
            (250, 100),
            self.fb_simulator,
        )
        self.next_game_button = MenuButton(
            "Start Game",
            (250, 150),
            self.fb_simulator,
        )

    def update(self, delta_time):
        if self.next_game_button.click():
            new_state = FootballGameState(self.fb_simulator)
            new_state.enter_state()

    def render(self, window):
        window.fill((0, 0, 0))
        self.team_name_banner.draw(window)
        self.roster_banner.draw(window)
        self.quarterback_button.draw(window)
        self.running_back_button.draw(window)
        self.wide_receiver_button.draw(window)
        self.linebacker_button.draw(window)
        self.defensive_back_button.draw(window)
        self.next_game_banner.draw(window)
        self.next_game_button.draw(window)
