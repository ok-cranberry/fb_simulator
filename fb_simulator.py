import positions
import playfromscrimmage


def main():

    QB = positions.Quarterback("Charlie Manack")
    WR = positions.WideReceiver("Hunter Patterson")
    DB = positions.DefensiveBack("Chris Pierce")

    play = playfromscrimmage.PlayFromScrimmage(20, QB, WR, DB)
    play.play()


if __name__ == "__main__":
    main()
