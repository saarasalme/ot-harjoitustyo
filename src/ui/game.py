import pygame
from ..entities.snacks import Snacks
from ..logic.mover import Mover

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("RoniPoika")

        self.roni = pygame.image.load("./resources/Roni.JPG")
        self.sausage = pygame.image.load("./resources/Nakki.JPG")
        self.meatball = pygame.image.load("./resources/Pulla.JPG")
        self.treat = pygame.image.load("./resources/Naksu.JPG")

        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.snacks = Snacks()
        self.mover = Mover()

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.roni_x = 300
        self.roni_y = 200

        self.speed = 3

    def new_game(self):
        return

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_DOWN:
                    self.down = True
                if event.key == pygame.K_UP:
                    self.up = True

                if event.key == pygame.K_SPACE:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False
                if event.key == pygame.K_DOWN:
                    self.down = False
                if event.key == pygame.K_UP:
                    self.up = False

        self.mover.move_roni()
        self.snacks.add_snack()
        for snack in self.snacks.sausages:
            self.mover.move_snack(snack)
        for snack in self.snacks.meatballs:
            self.mover.move_snack(snack)
        for snack in self.snacks.treats:
            self.mover.move_snack(snack) 

    def draw_screen(self):
        while True:
            self.screen.fill((255, 204, 233))
            self.screen.blit(self.roni, (self.roni_x, self.roni_y))
            for snack in self.snacks.sausages:
                self.screen.blit(self.sausage, (snack[0], snack[1]))
            for snack in self.snacks.meatballs:
                self.screen.blit(self.meatball, (snack[0], snack[1]))
            for snack in self.snacks.treats:
                self.screen.blit(self.treat, (snack[0], snack[1]))
            pygame.display.flip()
            self.clock.tick(60)


            self.move_roni()