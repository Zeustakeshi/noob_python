import pygame, sys, random
from Dino import Dino
from Floor import Floor

class Game:
    def __init__ (self):
        pygame.init()
        self.game_width = 600
        self.game_height = 800
        self.screen = pygame.display.set_mode((self.game_width, self.game_height))
        self.game_exit = False
        self.gravity = 1
        self.game_active = True
        self.score = 0
        self.high_score = 0
        self.dino_movement = 0

        # Game object
        self.floor = Floor(self)
        self.dino = Dino(self) 

        # Game loop
        while not self.game_exit:
            self.event_listener()
            self.update()
            #pygame.display.update() = pygame.display.flip() (hai ham nay giong nhau)
            pygame.display.flip()
        pygame.quit()
        sys.exit()

    def event_listener (self):
        for event in pygame.event.get():
            #When click close button
            if event.type == pygame.QUIT:
                self.game_exit = True
            self.dino.event_listener(event)

    def draw (self):
        # Clear screen 
        self.screen.fill((255, 255, 255))
        self.floor.draw()
        self.dino.draw()
    
    def update (self):
        self.dino.update()
        self.draw()




















    





