import random
import time


class GameClock:
    def __init__(self):
        self.quarter_length_minutes = 12
        self.current_time = self.quarter_length_minutes * 60
        self.next_event_time = self.current_time
        # self.dt = 0
        self.prev_time = time.time()
        self.second_overflow = 0

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
            # self.next_event_time = 0
        else:
            self.current_time -= time

            # trying to implment the look ahead in the simulation
            # self.next_event_time -= time

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

    def reset_clock_for_quarter(self):
        """resets the game clock to self.quarter_length_minutes"""
        self.current_time = self.quarter_length_minutes * 60

    def update_program_time(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def clock_countdown(self, game_speed_modifer=1000):
        """updates the GameClock sec by sec for a countdown effect"""

        self.update_program_time()
        dt = game_speed_modifer * self.dt

        self.second_overflow += dt
        if self.second_overflow > 10:
            self.second_overflow -= 10
            self.current_time -= 1
