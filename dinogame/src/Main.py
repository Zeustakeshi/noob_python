import pygame, sys, random
from Dino import Dino
from Floor import Floor

class Game:
    def __init__ (self):
        pygame.init()
        self.game_width = 600
        self.game_height = 800

        self.screen = pygame.display.set_mode((self.game_width, self.game_height))
        self.gravity = 0.25
        self.game_avt = True
        self.score = 0
        self.high_score = 0
        self.dino_movement = 0

        # Game obj
        self.floor = Floor(self)
        self.dino = Dino(self) 

        #draw game obj
        self.draw()
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.update()
            self.draw()
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def draw (self):
        self.dino.draw()
        self.floor.draw()
    
    def update (self):
        self.dino.y -= 11
        # self.dino.update()




















    





