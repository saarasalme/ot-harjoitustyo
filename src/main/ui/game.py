import pygame
from main.entities.snacks import Snacks
from main.logic.mover import Mover
from main.logic.collision import Collision

class Game:
    """ Class for running the game  """

    def __init__(self):
        """ The class constructor """

        pygame.init()
        pygame.display.set_caption("RoniPoika")

        self.roni1 = pygame.image.load("./resources/roni_pieni1_63x40.png")
        self.roni2 = pygame.image.load("./resources/roni_pieni2_79x50.png")
        self.roni3 = pygame.image.load("./resources/roni_iso_88x60.png")
        self.roni1_right = pygame.image.load("./resources/roni_pieni1_oikea63x40.png")
        self.roni2_right = pygame.image.load("./resources/roni_pieni2_oikea79x50.png")
        self.roni3_right = pygame.image.load("./resources/roni_iso_oikea88x60.png")
        self.right_picture = False
        self.snack1 = pygame.image.load("./resources/snack1_18x20.png")
        self.snack2 = pygame.image.load("./resources/snack2_23x40.png")
        self.snack3 = pygame.image.load("./resources/snack3_29x55.png")
        self.snack4 = pygame.image.load("./resources/snack4_95x50.png")

        self.screen = pygame.display.set_mode((640, 480))
        self.font = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()

        self.mover = Mover()
        self.collision = Collision()

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.roni_x = 300
        self.roni_y = 200

        self.high_score = 0
        self.game_state = 0
        self.level = 1


    def new_game(self):
        """ Method to start the game """

        self.game_state = 1
        self.snacks = Snacks()
        self.score = 0
        self.level = 1


    def handle_events(self):
        """ Method to check and handle every game event """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                    self.right_picture = False
                if event.key == pygame.K_RIGHT:
                    self.right = True
                    self.right_picture = True
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

        if self.game_state == 1:
            new_x_y = self.mover.move_roni(self.left, self.right, self.down, self.up, self.roni_x, self.roni_y, self.level)
            self.roni_x = new_x_y[0]
            self.roni_y = new_x_y[1]

            self.snacks.add_snack(self.level)
            for snack in self.snacks.snacks:
                self.mover.move_snack(snack)
                if self.collision.if_hits(snack, self.roni_x, self.roni_y, self.level):
                    if snack[3] <= self.level:
                        self.score += 1
                        self.snacks.snacks.remove(snack)
                        if self.score / 10 == self.level:
                            self.level += 1
                            if self.level == 4:
                                self.game_state = 3
                    else:
                        self.game_state = 2
                if self.collision.if_out_of_screen(snack):
                    self.snacks.snacks.remove(snack)
                    

    def start_screen(self):
        """ This method draws the start screen """

        pygame.draw.rect(self.screen, (247,176,211), (90,90,460,300))
        start_text = self.font.render("Unohdit ruokkia koiran! Kerää herkkuja,", True, (0,0,0))
        self.screen.blit(start_text, (105,110))
        start_text = self.font.render("jotta koira ei kuole nälkään.", True, (0,0,0))
        self.screen.blit(start_text, (105,140))
        start_text = self.font.render("Aloita peli = SPACE", True, (0,0,0))
        self.screen.blit(start_text, (220,260))

    def game_screen(self):
        """ This method draws the game screen """
        if self.level == 1:
            if self.right_picture:
                self.screen.blit(self.roni1_right, (self.roni_x, self.roni_y))
            else:   
                self.screen.blit(self.roni1, (self.roni_x, self.roni_y))
        elif self.level == 2:
            if self.right_picture:
                self.screen.blit(self.roni2_right, (self.roni_x, self.roni_y))
            else:
                self.screen.blit(self.roni2, (self.roni_x, self.roni_y))
        else:
            if self.right_picture:
                self.screen.blit(self.roni3_right, (self.roni_x, self.roni_y))
            else:
                self.screen.blit(self.roni3, (self.roni_x, self.roni_y))
        for snack in self.snacks.snacks:
            if snack[3] == 1:
                self.screen.blit(self.snack1, (snack[0], snack[1]))
            elif snack[3] == 2:
                self.screen.blit(self.snack2, (snack[0], snack[1]))
            elif snack[3] == 3:
                self.screen.blit(self.snack3, (snack[0], snack[1]))
            elif snack[3] == 4:
                self.screen.blit(self.snack4, (snack[0], snack[1]))

        score_text = self.font.render(f"Taso: {self.level}  Pisteet: {self.score}", True, (0,0,0))
        self.screen.blit(score_text, (440, 10))

    def end_screen_lose(self):
        """ This method draws the end screen when player loses"""

        pygame.draw.rect(self.screen, (247,176,211), (90,90,460,300))
        end_text = self.font.render(f"Peli päättyi, pisteet: {self.score}", True, (0,0,0))
        self.screen.blit(end_text, (150,200))
        end_text = self.font.render("Uusi peli = SPACE, Sulje peli = Esc", True, (0,0,0))
        self.screen.blit(end_text, (150,240))
        end_text = self.font.render(f"Sinun tulos = {self.score}  Paras tulos = {self.high_score}", True, (0,0,0))
        self.screen.blit(end_text, (160,280))

    def end_screen_win(self):
        """ This method draws the end screen when player wins """

        pygame.draw.rect(self.screen, (170,210,235), (90,90,460,300))
        end_text = self.font.render("Onneksi olkoon! Sait", True, (0,0,0))
        self.screen.blit(end_text, (105,110))
        end_text = self.font.render("ruokittua koiran", True, (0,0,0))
        self.screen.blit(end_text, (105,140))
        end_text = self.font.render("Uusi peli = SPACE", True, (0,0,0))
        self.screen.blit(end_text, (220,260))
        end_text = self.font.render(f"Sinun tulos = {self.score}  Paras tulos = {self.high_score}", True, (0,0,0))
        self.screen.blit(end_text, (160,280))
        self.screen.blit(self.snack4, (350, 135))
        self.screen.blit(self.roni3, (440,100))


    def draw_screen(self):
        """ This method draws screen """
        if self.level < 3:
            self.screen.fill((255, 204, 233))
        else:
            self.screen.fill((160,205,227))
        if self.game_state == 0:
            self.start_screen()
        if self.game_state == 1:
            self.game_screen()
        if self.game_state == 2:
            self.end_screen_lose()
        if self.game_state == 3:
            self.end_screen_win()

        pygame.display.flip()
        self.clock.tick(60)
