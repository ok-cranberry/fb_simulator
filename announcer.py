class Announcer:
    """
    Serves as the game log, outputing game events to the game loop for display on screen
    """

    def __init__(self):
        self.game_log = []

    def store_commentary(self, line_of_commentary: str):
        self.game_log.append(line_of_commentary)

    def return_commentary(self):

        if self.game_log:
            return self.game_log[-1]
        else:
            return "-"
