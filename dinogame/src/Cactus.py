import random, pygame

class Cactus: 
    def __init__ (self, game):
        self.game = game

        self.colors = ["#059669", "#e11d48", "#10b981"]
        self.color = self.colors[random.randint(0, len(self.colors) - 1)]

        self.width = 30
        self.min_height = 40
        self.max_height = 100
        self.height = random.randint(self.min_height, self.max_height)
        self.x = self.game.game_width
        self.y = self.game.game_height - (self.game.floor_height + self.height)
        
    
    def draw (self):
        rect = pygame.Rect(self.x, self.y , self.width, self.height)
        pygame.draw.rect(self.game.screen, self.color, rect)

    def update (self):
        self.x -= self.game.speed
        if (self.x + self.width < 0): 
            self.color = self.colors[random.randint(0, len(self.colors) - 1)]
            self.height = random.randint(self.min_height, self.max_height)
            self.y = self.game.game_height - (self.game.floor_height + self.height)
            self.x = self.game.game_width
