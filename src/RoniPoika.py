import pygame
from random import randint, choice

class Game:
    def __init__(self):
        pygame.init()
        self.roni = pygame.image.load("Roni.JPG")
        self.sausage = pygame.image.load("Nakki.JPG")
        self.meatball = pygame.image.load("Pulla.JPG")
        self.treat = pygame.image.load("Naksu.JPG")
        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()

    def draw_screen(self):
        while True:
            self.screen.fill((30,30,30))
            self.screen.blit(self.roni, (300,200))
            self.screen.blit(self.sausage,(100,100))
            self.screen.blit(self.meatball,(450,100))
            self.screen.blit(self.treat,(350,100))
            pygame.display.flip()
            self.clock.tick(60)
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    exit()

class Snacks:
    def __init__(self):
        self.sausages = []
        self.meatballs = []
        self.treats = []

    def add_snack(self):
        snack = choice([self.sausages, self.meatballs, self.treats])
        snack.append([randint(0,640),randint(0,480)])


        
        
if __name__=="__main__":

    g = Game()
    g.draw_screen()
