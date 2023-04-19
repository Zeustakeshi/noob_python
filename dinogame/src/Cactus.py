import random, pygame

class Cactus: 
    def __init__ (self, game):
        self.game = game

        self.scale = 0.1
        self.images = []
        self.load_image()
        self.image = self.images[random.randint(0, len(self.images) - 1)]

        self.width = self.image.get_width() 
        self.height = self.image.get_height() 
        self.x = self.game.game_width
        self.y = self.game.game_height - (self.game.floor_height + self.height)
        self.collisionX = self.x
        self.collisionY = self.y
 


    def load_image (self):
        for i in range (1, 6):
            image = pygame.image.load("./assets/mushroom_spotted_" + str(i) + ".png")
            image = pygame.transform.scale(image, (image.get_width() * self.scale, image.get_height() * self.scale))
            self.images.append(image)
    

    def reset_state (self):
        self.image = self.images[random.randint(0, len(self.images) - 1)]
        self.width = self.image.get_width() 
        self.height = self.image.get_height() 
        self.y = self.game.game_height - (self.game.floor_height + self.height)
        self.x = self.game.game_width
        self.game.score = self.game.score + 1
        self.collisionX = self.x
        self.collisionY = self.y

    def draw (self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def update (self):
        self.x -= self.game.speed
        if (self.x + self.width < 0): self.reset_state()
        #check collision with dino
        # if (self.game.check_collision(self, self.game.dino)):
        #     self.game.game_active = False

        self.collisionX = self.x
        self.collisionY = self.y
