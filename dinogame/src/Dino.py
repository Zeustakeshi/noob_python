import pygame

class Dino :
    def __init__ (self, game):
        self.game = game
        self.sprire_width = 803
        self.sprire_height = 1330
        self.scale = 0.12
        self.width = self.sprire_width * self.scale
        self.height = self.sprire_height * self.scale
        

        self.x = 50
        self.y = self.game.game_height - (self.game.floor_height + self.height)
        self.collisionX = self.x
        self.collisionY = self.y
        self.color = "skyblue"

        # xu li anh
        self.image = pygame.image.load("./assets/toad_antennae.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.flip(self.image, True, False)

        #suc nhay cua dino
        self.jump_force = 250
        self.is_on_ground = True
    
    
    def event_listener (self, event):
        if event.type == pygame.KEYDOWN:
            #When key press W or SPACE
            if (event.key == pygame.K_SPACE or event.key == pygame.K_w) and self.game.game_active and self.is_on_ground:
                self.y -= self.jump_force
                self.is_on_ground = False

    def draw (self): 
        self.game.screen.blit(self.image, (self.x, self.y))

    def update (self):
        ground = self.game.game_height - (self.game.floor_height + self.height)

        # kiem tra xem co tren mat dat hay khong
        if (self.y >= ground): 
            self.is_on_ground = True
            self.y = ground
        else:
            self.y += self.game.gravity 

        