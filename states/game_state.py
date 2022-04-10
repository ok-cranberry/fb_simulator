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
