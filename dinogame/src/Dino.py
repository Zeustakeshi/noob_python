import pygame

class Dino :
    def __init__ (self, game):
        self.game = game
        self.width = 50
        self.height = 50
        self.x = 50
        self.y = self.game.game_height - (self.game.floor.height + self.height)
        self.color = "skyblue"
        self.jump_force = 100
        self.is_on_ground = True
    
    def event_listener (self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.game.game_active and self.is_on_ground:
                self.y -= self.jump_force
                self.is_on_ground = False

    def draw (self): 
        rect = pygame.Rect(self.x, self.y , self.width, self.height)
        pygame.draw.rect(self.game.screen, self.color, rect)

    def update (self):
        ground = self.game.game_height - (self.game.floor.height + self.height)

        # kiem tra xem co tren mat dat hay khong
        if (self.y >= ground): 
            self.is_on_ground = True
        else:
            self.y += self.game.gravity 

        