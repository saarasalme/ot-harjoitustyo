from src.ui.game import Game

class RoniPoika():
    def __init__(self):
        self.game = Game()

    def loop(self):
        while True:
            self.game.handle_events()
            self.game.draw_screen()

if __name__ == "__main__":    
    r = RoniPoika()
    r.loop()
#    g = Game()
#    g.draw_screen()

