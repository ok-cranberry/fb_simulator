from states.game_state import GameState
from menu_button import MenuButton
from states.team_selection_state import TeamSelectionState


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
