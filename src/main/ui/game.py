import pygame
import time
import os
import csv
from functools import cmp_to_key
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
        
        self.game_state = 0
        self.time_score = 0

        self.level = 1


    def new_game(self):
        """ Method to start the game """

        self.game_state = 1
        self.snacks = Snacks()
        self.score = 0
        self.level = 1
        self.start_time = time.time()

    def high_score_write(self):


        dirname = os.path.dirname(__file__)
        self.high_score = open(os.path.join(dirname,"../../../resources/highscore.csv"), "a+")
        text = f"{self.score},{self.time_score:.1f}\n"
        self.high_score.write(text)
        self.high_score_read()
        self.high_score.close()

    def high_score_read(self):
        def sort_function(a, b):
            """ 
            Compares values in the high score file.
            If point total is the same, compares time and orders from smallest to biggest

            Args:
                a - first list to compare
                b - second list to compare
            Returns:
                0 if equal, 1 if larger, -1 if smaller
            """
            if float(a[0]) == float(b[0]):
                if float(a[1]) == float(b[1]):
                    return 0
                if float(a[1]) > float(b[1]):
                    return -1
                return 1
            if float(a[0]) > float(b[0]):
                return 1
            return -1
        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname,"../../../resources/highscore.csv"), mode= "r") as high_score_file:
            csv_file = csv.reader(high_score_file)
            return sorted(csv_file, reverse= True, key=cmp_to_key(sort_function))
        
    

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
                if event.key == pygame.K_s:
                    if self.game_state == 4:
                        self.game_state = 0
                    elif self.game_state != 1:
                        self.game_state = 4
                if event.key == pygame.K_o:
                    if self.game_state == 5:
                        self.game_state = 0
                    else:
                        self.game_state = 5
                
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
                                self.high_score_write()
                    else:
                        self.game_state = 2
                        self.high_score_write()
                if self.collision.if_out_of_screen(snack):
                    self.snacks.snacks.remove(snack)
                    
            time_now = time.time()
            self.time_score = time_now - self.start_time


    def start_screen(self):
        """ Method to draw the start screen """

        pygame.draw.rect(self.screen, (247,176,211), (90,90,460,300))
        start_text = self.font.render("Unohdit ruokkia koiran! Kerää herkkuja,", True, (0,0,0))
        self.screen.blit(start_text, (105,110))
        start_text = self.font.render("jotta koira ei kuole nälkään.", True, (0,0,0))
        self.screen.blit(start_text, (105,140))
        start_text = self.font.render("Väistele isompia herkkuja!", True, (0,0,0))
        self.screen.blit(start_text, (105,170))
        start_text = self.font.render("Parhaat tulokset = S", True, (0,0,0))
        self.screen.blit(start_text, (220,300))
        start_text = self.font.render("Aloita peli = SPACE", True, (0,0,0))
        self.screen.blit(start_text, (220,260))
        start_text = self.font.render("Ohjeet = O", True, (0,0,0))
        self.screen.blit(start_text, (220,340))

    def game_screen(self):
        """ Method to draw the game screen """

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

        score_text = self.font.render(f"Taso: {self.level}  Pisteet: {self.score}  Aika: {self.time_score:.1f}", True, (0,0,0))
        self.screen.blit(score_text, (300, 10))

    def end_screen_lose(self):
        """ Method to draw the end screen when player loses"""

        pygame.draw.rect(self.screen, (247,176,211), (90,90,460,300))
        end_text = self.font.render(f"Yritit haukata vähän liian ison palan :(", True, (0,0,0))
        self.screen.blit(end_text, (120,160))
        end_text = self.font.render("Uusi peli = SPACE, Sulje peli = Esc", True, (0,0,0))
        self.screen.blit(end_text, (120,220))
        end_text = self.font.render("Parhaat tulokset = S, Ohjeet = O", True, (0,0,0))
        self.screen.blit(end_text, (120,250))
        end_text = self.font.render(f"Sinun tulos = {self.score}p {self.time_score:.1f}s  ", True, (0,0,0))
        self.screen.blit(end_text, (150,300))
        best_score = self.high_score_read()
        end_text = self.font.render(f"Paras tulos = {best_score[0][0]}p {best_score[0][1]}s", True, (0,0,0))
        self.screen.blit(end_text, (150,340))


    def end_screen_win(self):
        """ Method to draw the end screen when player wins """

        pygame.draw.rect(self.screen, (170,210,235), (90,90,460,300))
        end_text = self.font.render("Onneksi olkoon! Sait", True, (0,0,0))
        self.screen.blit(end_text, (105,110))
        end_text = self.font.render("ruokittua koiran", True, (0,0,0))
        self.screen.blit(end_text, (105,140))
        end_text = self.font.render("Uusi peli = SPACE, Parhaat tulokset = S", True, (0,0,0))
        self.screen.blit(end_text, (105,240))
        end_text = self.font.render(f"Sinun tulos = {self.score}p {self.time_score:.1f}s  ", True, (0,0,0))
        self.screen.blit(end_text, (150,300))
        best_score = self.high_score_read()
        end_text = self.font.render(f"Paras tulos = {best_score[0][0]}p {best_score[0][1]}s", True, (0,0,0))
        self.screen.blit(end_text, (150,340))
        self.screen.blit(self.snack4, (350, 135))
        self.screen.blit(self.roni3, (440,100))

    def high_score_screen(self):
        """ Method to draw the high score screen"""

        pygame.draw.rect(self.screen, (247,176,211), (90,90,460,300))
        score_text = self.font.render("Parhaat tulokset:", True, (0,0,0))
        self.screen.blit(score_text, (105,110))
        best_score = self.high_score_read()
        if len(best_score) >= 5:
            for i in range(5):
                score_text = self.font.render(f"{i+1}. {best_score[i][0]}p,  {best_score[i][1]}s", True, (0,0,0))
                self.screen.blit(score_text, (130,150 + i * 30))
        else:
            for i in range(len(best_score)):
                score_text = self.font.render(f"{i+1}. {best_score[i][0]}p,  {best_score[i][1]}s", True, (0,0,0))
                self.screen.blit(score_text, (130,150 + i * 30))
        score_text = self.font.render("Uusi peli = SPACE", True, (0,0,0))
        self.screen.blit(score_text, (220,310)) 
        score_text = self.font.render("Aloitusruutu = S", True, (0,0,0))
        self.screen.blit(score_text, (220,335))
        score_text = self.font.render("Ohjeet = O", True, (0,0,0))
        self.screen.blit(score_text, (220,360))   

    def guide_screen(self):
        """ Method to draw guide screen """

        pygame.draw.rect(self.screen, (247,176,211), (90,90,460,300))
        guide_text = self.font.render("Ohjeet:", True, (0,0,0))
        self.screen.blit(guide_text, (100,110))
        guide_text = self.font.render("Liikuta koiraa nuolinäppäimillä. Voit ", True, (0,0,0))
        self.screen.blit(guide_text, (100,150))
        guide_text = self.font.render("syödä korkeintaan saman tason herkkuja.", True, (0,0,0))
        self.screen.blit(guide_text, (100,180))
        guide_text = self.font.render("1.", True, (0,0,0))
        self.screen.blit(guide_text, (140,220))
        self.screen.blit(self.snack1, (190,220))
        guide_text = self.font.render("2.", True, (0,0,0))
        self.screen.blit(guide_text, (140,260))
        self.screen.blit(self.snack2, (190,260))
        guide_text = self.font.render("3.", True, (0,0,0))
        self.screen.blit(guide_text, (140,300))
        self.screen.blit(self.snack3, (190,310))
        guide_text = self.font.render("Uusi peli = SPACE", True, (0,0,0))
        self.screen.blit(guide_text, (300,300))
        guide_text = self.font.render("Aloitusruutu = O", True, (0,0,0))
        self.screen.blit(guide_text, (300,340))


    def draw_screen(self):
        """ Method to draw screen """
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
        if self.game_state == 4:
            self.high_score_screen()
        if self.game_state == 5:
            self.guide_screen()

        pygame.display.flip()
        self.clock.tick(60)
