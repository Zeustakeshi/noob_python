import pygame
class Floor: 
    def __init__ (self, game ) :
        self.game = game
        self.width = self.game.game_width
        self.height = self.game.floor_height
        self.x = 0
        self.y = self.game.game_height - self.height
        self.color = "tomato"
        
    def draw (self):
        rect = pygame.Rect(self.x, self.y , self.width, self.height)
        pygame.draw.rect(self.game.screen, self.color, rect)

    def update (self):
        print("dino update")

