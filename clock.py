class GameClock:
    def __init__(self):
        self.quarter_length_minutes = 12
        self.current_time = self.quarter_length_minutes * 60

    def format_clock(self, clock_value):
        """Outputs the minutes and seconds in MM:SS form"""

        minute = clock_value / 60
        seconds = clock_value % minute

        return f"{minute}:{second}"

    def update_clock(self):
        """Updates the current time remaining in the quarter"""
        pass

    def play_duration(self):
        """determines the time elapsed during a single play"""
        pass

    def intra_play_duration(self):
        """determines the time from tackle, huddle, to snap"""
        pass

    def get_current_time(self):
        """returns the current time left in the quarter (in seconds)"""

        return self.current_time
