import play as p


class Drive:
    def __init__(self, starting_yardline, quarterback, wide_receiver, defensive_back):
        self.starting_yardline = starting_yardline
        self.current_yardline = starting_yardline
        self.quarterback = quarterback
        self.wide_receiver = wide_receiver
        self.defensive_back = defensive_back

        self.drive_yardage = 0
        self.score = 0

    def update_distance(self, line_of_scrimmage, yards_gained):
        """Update the down, distance, and score"""
        line_of_scrimmage += yards_gained
        return line_of_scrimmage

    def update_down(self, down, yards_to_1st_down, yards_gained):
        """Update the numbered down.  Plays of 10 yards are more reset the down to 1. Plays less than 10 yards reduce the yards to gain until 10 yards hve been gained"""
        if yards_gained < yards_to_1st_down:
            down += 1
            yards_to_1st_down -= yards_gained
        else:
            down = 1
            yards_to_1st_down = 10

        return down, yards_to_1st_down

    def drive(self):

        end_of_drive = False
        yardline = self.starting_yardline
        down = 1
        yards_to_1st_down = 10
        self.score = 0

        while end_of_drive is False:
            print(f"It's {down} down and {yards_to_1st_down}")
            play = p.Play(
                yardline,
                self.quarterback,
                self.wide_receiver,
                self.defensive_back,
            )
            yards_gained, turnover = play.run_play()
            self.drive_yardage += yards_gained

            yardline = self.update_distance(yardline, yards_gained)
            down, yards_to_1st_down = self.update_down(
                down, yards_to_1st_down, yards_gained
            )

            if turnover is True:
                end_of_drive = True
            if down > 4:
                print("That's a turnover on downs")
                end_of_drive = True
            if yardline >= 100:
                print("TOUCHDOWN!!")
                self.score += 7
                end_of_drive = True
