import pygame

class Camera:

    def __init__(self, width, height, game):
        self.game = game
        self.width = width
        self.height = height

        self.viewRect = pygame.Rect(0, 0, self.width, self.height)
    
    def apply(self, entity):
        return entity.rect.move(self.viewRect.topleft)
    
    def update(self, target):
        x = -target.rect.x + int(self.game.windowWidth / 2)
        y = -target.rect.y + int(self.game.windowHeight / 2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - self.game.windowWidth), x)
        y = max(-(self.height - self.game.windowHeight), y)

        self.viewRect = pygame.Rect(x, y, self.width, self.height)