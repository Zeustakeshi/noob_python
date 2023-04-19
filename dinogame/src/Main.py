import pygame, sys, random, math
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
        self.floor_height = 100
        self.speed = 10

        #TEXT 
        self.font = pygame.font.Font(None, 36)


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

    #def on_game_over (self):

    def check_collision (self, objectA, objectB):
        return (
           (objectA.collisionX > objectB.collisionX and objectA.collisionX < objectB.collisionX + objectB.width
           and objectA.collisionY > objectB.collisionY and objectA.collisionY < objectB.collisionY + objectB.height
           )or 
           (objectB.collisionX > objectA.collisionX and objectB.collisionX < objectA.collisionX + objectA.width
           and objectB.collisionY > objectA.collisionY and objectB.collisionY < objectA.collisionY + objectA.height
           )
        )

    def event_listener (self):
        for event in pygame.event.get():
            #When click close button
            if event.type == pygame.QUIT:
                self.game_exit = True
            self.dino.event_listener(event)


    def draw_game_status (self):
        text_surface = self.font.render("Score: " + str(self.score), True,pygame.Color("#0f172a"))
        self.screen.blit(text_surface, (40, 40))

    def draw (self):
        # Clear screen 
        self.screen.fill((255, 255, 255))
        self.draw_game_status()
        #draw object
        self.floor.draw()
        self.dino.draw()
        for obstacle in self.obstacles: obstacle.draw()
    
    def update (self):
        self.dino.update()
        for obstacle in self.obstacles: obstacle.update()
        self.draw()




















    





