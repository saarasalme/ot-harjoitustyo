import pygame

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

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.roni_x = 300
        self.roni_y = 200

        self.speed = 2

    def new_game(self):
        return

    def move_roni(self):
        if self.left:
            if self.roni_x > 0:
                self.roni_x -= self.speed
        if self.right:
            if self.roni_x < 640 - self.roni.get_width():
                self.roni_x += self.speed
        if self.down:
            if self.roni_y < 480 - self.roni.get_height():
                self.roni_y += self.speed
        if self.up:
            if self.roni_y > 0:
                self.roni_y -= self.speed

    def draw_screen(self):
        while True:
            self.screen.fill((255, 204, 233))
            self.screen.blit(self.roni, (self.roni_x, self.roni_y))
            self.screen.blit(self.sausage, (100, 100))
            self.screen.blit(self.meatball, (450, 100))
            self.screen.blit(self.treat, (350, 100))
            pygame.display.flip()
            self.clock.tick(60)
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

            self.move_roni()