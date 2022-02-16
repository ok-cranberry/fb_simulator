import random


class GameClock:
    def __init__(self):
        self.quarter_length_minutes = 12
        self.current_time = self.quarter_length_minutes * 60

    def format_clock(self):
        """Outputs the minutes and seconds in MM:SS form"""

        clock_value = self.current_time

        minute = int(clock_value / 60)
        second = clock_value - (minute * 60)

        return f"{minute}:{second:02d}"

    def update_clock(self, time: int):
        """Updates the current time remaining in the quarter"""
        # If the elapsed time is greater than the time left, return 0:00
        if self.current_time < time:
            self.current_time = 0
        else:
            self.current_time -= time

    def play_duration(self, time: int):
        """determines the time elapsed during a single play"""
        duration = time + random.randint(-2, 2)
        self.update_clock(duration)

    def intra_play_duration(self, time: int):
        """determines the time from tackle, huddle, to snap"""
        duration = time + random.randint(-10, 10)
        self.update_clock(duration)

    def get_current_time(self):
        """returns the current time left in the quarter (in seconds)"""

        return self.current_time
