from states.game_state import GameState
from menu_button import MenuButton
import states.team_overview_state


class GameEndState(GameState):
    def __init__(self, fb_simulator):
        GameState.__init__(self, fb_simulator)

        self.return_to_team_button = MenuButton(
            "Return", (0, 0), self.fb_simulator
        )

    def update(self, delta_time):
        if self.return_to_team_button.click():
            new_state = states.team_overview_state.TeamOverviewState(
                self.fb_simulator
            )
            new_state.enter_state()

    def render(self, window):
        self.return_to_team_button.draw(window)
