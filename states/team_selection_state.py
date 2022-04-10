from states.game_state import GameState
from states.team_overview_state import TeamOverviewState
from menu_button import MenuButton
from league import League
from team import Team


class TeamSelectionState(GameState):
    def __init__(self, fb_simulator):
        GameState.__init__(self, fb_simulator)

        self.conference = League(
            (
                Team("Frazier"),
                Team("Geibel"),
                Team("Monessen"),
                Team("West Greene"),
            )
        )

        self.team_1_button = MenuButton(
            "Frazier", (100, 200), self.fb_simulator
        )
        self.team_2_button = MenuButton(
            "Geibel", (100, 250), self.fb_simulator
        )
        self.team_3_button = MenuButton(
            "Monesson", (100, 300), self.fb_simulator
        )
        self.team_4_button = MenuButton(
            "West Greene", (100, 350), self.fb_simulator
        )

    def update(self, delta_time):
        if self.team_1_button.click():
            self.fb_simulator.player_team = self.conference.teams[0]
            new_state = TeamOverviewState(self.fb_simulator)
            new_state.enter_state()
        if self.team_2_button.click():
            self.fb_simulator.player_team = self.conference.teams[1]
            new_state = TeamOverviewState(self.fb_simulator)
            new_state.enter_state()
        if self.team_3_button.click():
            self.fb_simulator.player_team = self.conference.teams[2]
            new_state = TeamOverviewState(self.fb_simulator)
            new_state.enter_state()
        if self.team_4_button.click():
            self.fb_simulator.player_team = self.conference.teams[3]
            new_state = TeamOverviewState(self.fb_simulator)
            new_state.enter_state()

    def render(self, window):
        window.fill((0, 0, 0))
        self.team_1_button.draw(window)
        self.team_2_button.draw(window)
        self.team_3_button.draw(window)
        self.team_4_button.draw(window)
