import play as p
from team import Team


class Drive:
    def __init__(self, starting_yardline, offense: Team, defense: Team):
        self.starting_yardline = starting_yardline
        self.current_yardline = starting_yardline
        self.offense = offense
        self.defense = defense

        self.drive_yardage = 0
        self.score = 0

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

        end_of_drive = False
        down = 1
        yards_to_1st_down = 10
        self.score = 0

        while end_of_drive is False:
            print(f"It's {down} down and {yards_to_1st_down}")
            play = p.Play(
                self.current_yardline,
                self.offense,
                self.defense,
            )
            yards_gained, turnover = play.run_play()
            self.drive_yardage += yards_gained

            self.current_yardline = self.update_distance(
                self.current_yardline, yards_gained
            )
            down, yards_to_1st_down = self.update_down(
                down, yards_to_1st_down, yards_gained
            )

            if turnover is True:
                end_of_drive = True
            if down > 4:
                print("That's a turnover on downs")
                end_of_drive = True
            if self.current_yardline >= 100:
                print("TOUCHDOWN!!")
                self.score += 7
                end_of_drive = True
