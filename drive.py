from announcer import Announcer
from clock import GameClock
from play import Play
from team import Team


class Drive:
    def __init__(
        self,
        starting_yardline,
        offense: Team,
        defense: Team,
        clock: GameClock,
        announcer: Announcer,
    ):
        self.starting_yardline = starting_yardline
        self.current_yardline = starting_yardline
        self.offense = offense
        self.defense = defense
        self.clock = clock
        self.announcer = announcer

        self.end_of_drive = False
        self.drive_yardage = 0
        self.score = 0

        self.turnover = False
        self.yards_gained = 0
        self.down = 1
        self.yards_to_1st_down = 10

    def update_distance(self, line_of_scrimmage, yards_gained):
        """Update the down, distance, and score"""
        line_of_scrimmage += yards_gained
        return line_of_scrimmage

    def update_down(self, down, yards_to_1st_down, yards_gained):
        """Update the numbered down.  Plays of 10 yards are more reset the down
        to 1. Plays less than 10 yards reduce the yards to gain until 10 yards
        have been gained"""
        if yards_gained < yards_to_1st_down:
            down += 1
            yards_to_1st_down -= yards_gained
        else:
            down = 1
            yards_to_1st_down = 10

        return down, yards_to_1st_down

    def drive(self):

        self.end_of_drive = False
        down = 1
        yards_to_1st_down = 10
        self.score = 0

        if self.clock.get_current_time() is 0:
            end_of_drive = True

        while end_of_drive is False:
            print(f"It's {down} down and {yards_to_1st_down}")
            play = Play(
                self.current_yardline, self.offense, self.defense, self.clock
            )
            yards_gained, turnover = play.start_play()
            self.drive_yardage += yards_gained

            self.current_yardline = self.update_distance(
                self.current_yardline, yards_gained
            )
            down, yards_to_1st_down = self.update_down(
                down, yards_to_1st_down, yards_gained
            )

            if turnover is True:
                self.end_of_drive = True
            if down > 4:
                print("That's a turnover on downs")
                end_of_drive = True
            if self.current_yardline >= 100:
                print("TOUCHDOWN!!")
                self.score += 7
                end_of_drive = True
            if self.clock.get_current_time() is 0:
                end_of_drive = True

    def continue_drive(self):

        if self.end_of_drive is False:
            # output down and distance to screen
            play = Play(
                self.current_yardline,
                self.offense,
                self.defense,
                self.clock,
                self.announcer,
            )
            self.yards_gained, self.turnover = play.start_play()

            self.current_yardline = self.update_distance(
                self.current_yardline, self.yards_gained
            )
            self.down, self.yards_to_1st_down = self.update_down(
                self.down, self.yards_to_1st_down, self.yards_gained
            )

            if self.turnover is True:
                self.end_of_drive = True
            if self.down > 4:
                self.announcer.store_commentary("That's a turnover on downs")
                print("That's a turnover on downs")
                self.end_of_drive = True
            if self.current_yardline >= 100:
                self.announcer.store_commentary("TOUCHDOWN!!")
                print("TOUCHDOWN!!")
                self.score += 7
                self.end_of_drive = True
            if self.clock.get_current_time() is 0:
                self.end_of_drive = True
