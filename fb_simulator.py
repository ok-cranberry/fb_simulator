import positions
import drive as d


def main():

    QB = positions.Quarterback("Charlie Manack")
    WR = positions.WideReceiver("Hunter Patterson")
    DB = positions.DefensiveBack("Chris Pierce")

    drive = d.Drive(20, QB, WR, DB)
    drive.drive()


if __name__ == "__main__":
    main()
