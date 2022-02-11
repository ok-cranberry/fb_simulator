import play as p

class Drive:
    def __init__(self, starting_yardline, quarterback, wide_receiver, defensive_back):
        self.starting_yardline = starting_yardline
        self.quarterback = quarterback
        self.wide_receiver = wide_receiver
        self.defensive_back = defensive_back

        drive_yardage = 0



# capture the total yards of the Drive
# capture the number of drives a team has had
# capture 4 downs logic

# initialize the drives
# add a play
# capture the result of a play
# add that result to initialize the next play
# end it with a turnover, punt, or TD

    def update_down_and_distance(self, line_of_scrimmage, yards_gained):
        """Update the down, distance, and score"""
        line_of_scrimmage += yards_gained
        return line_of_scrimmage

    def drive(self):

        end_of_drive = False
        yardline = self.starting_yardline
        while end_of_drive is False:

            play = p.Play(yardline, self.quarterback, self.wide_receiver, self.defensive_back)
            yards_gained, turnover = play.run_play()

            yardline = self.update_down_and_distance(yardline, yards_gained)
            if turnover is True:
                end_of_drive = True
            if yardline >= 100:
                print("TOUCHDOWN!!")
                end_of_drive = True
