from states.game_state import GameState
from menu_button import MenuButton


class TeamSelectionState(GameState):
    def __init__(self, fb_simulator):
        GameState.__init__(self, fb_simulator)

    def update(self, delta_time):
        pass

    def render(self, window):
        window.fill((0, 0, 0))
