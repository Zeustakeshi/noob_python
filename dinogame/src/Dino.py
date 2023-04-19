import pygame

class Dino :
    def __init__ (self, game):
        self.game = game
        self.width = 50
        self.height = 50
        self.x = 50
        self.y = self.game.game_height - (self.game.floor.height + self.height)
        self.color = "skyblue"

    
    def draw (self): 
        rect = pygame.Rect(self.x, self.y , self.width, self.height)
        pygame.draw.rect(self.game.screen, self.color, rect)

    def update (self):
        if self.game.game_avt:
            self.game.dino_movement += self.game.gravity
        self.y += 1

        

        