import pygame, random
from methods import filePath

class Item2(pygame.sprite.Sprite):

    itemGroup = pygame.sprite.Group()
    
    def __init__(self, itemName, game, prefix):
        super().__init__()
        self.displayName = " ".join(itemName.split(".png")[0].split("_")).title()
        self.codeName = "_".join(self.displayName.lower().split(" "))

        self.imagePath = str(prefix + itemName)

        self.image = pygame.image.load(str(filePath.path(self.imagePath)))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/1.5), int(self.image.get_height()/1.5)))

        self.game = game

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(int(game.windowWidth/game.numberOfTiles), int(game.windowWidth-self.image.get_width()-(game.windowWidth/game.numberOfTiles)))

        self.rect.y = random.randint(int(game.windowHeight/game.numberOfTiles), int(game.windowHeight-self.image.get_height()-(game.windowHeight/game.numberOfTiles)))
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)