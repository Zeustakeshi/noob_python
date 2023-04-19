import pygame, sys, random
from Dino import Dino
from Floor import Floor
from Cactus import Cactus

class Game:
    def __init__ (self):
        pygame.init()
        self.game_width = 900
        self.game_height = 800
        self.screen = pygame.display.set_mode((self.game_width, self.game_height))

        self.game_exit = False
        self.gravity = 10
        self.game_active = True
        self.score = 0
        self.high_score = 0
        self.floor_height = 200
        self.speed = 10

        # Game object
        self.floor = Floor(self)
        self.dino = Dino(self) 
        #chuong ngai vat
        self.number_of_obstacles = 1 
        self.obstacles = []

        #FPS
        self.clock = pygame.time.Clock()
        self.FPS = 30  

        # Game loop
        self.init_obstacles()
        self.run()

    def init_obstacles (self):
        for x in range(self.number_of_obstacles):
            self.obstacles.append(Cactus(self ))

    def run (self):
        while not self.game_exit:
            self.event_listener()
            self.update()
            #pygame.display.update() = pygame.display.flip() (hai ham nay giong nhau)
            pygame.display.flip()
            self.clock.tick(self.FPS)
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
        #draw object
        self.floor.draw()
        self.dino.draw()
        for obstacle in self.obstacles: obstacle.draw()
    
    def update (self):
        self.dino.update()
        for obstacle in self.obstacles: obstacle.update()
        self.draw()




















    





