from main.ui.game import Game

class RoniPoika():
    """ Class to run the game """

    def __init__(self):
        """ The class constructor """
        self.game = Game()

    def loop(self):
        """ Method to run the game """
        while True:
            self.game.handle_events()
            self.game.draw_screen()

if __name__ == "__main__":
    r = RoniPoika()
    r.loop()
