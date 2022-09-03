import pygame, random
from methods import filePath

class Item(pygame.sprite.Sprite):

    itemGroup = pygame.sprite.Group()
    
    def __init__(self, itemName, game, prefix):
        super().__init__()
        self.itemName = itemName

        self.displayName = " ".join(itemName.split(".png")[0].split("_")).title()
        self.codeName = "_".join(self.displayName.lower().split(" "))

        self.imagePath = str(prefix + itemName)

        self.game = game

        self.image = pygame.image.load(str(filePath.path(self.imagePath)))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/1.5), int(self.image.get_height()/1.5)))

        self.rect = self.image.get_rect()


        self.rect.x = random.randint(self.game.map.tileWidth, self.game.map.width - self.image.get_width() - self.game.map.tileWidth)
        self.rect.y = random.randint(self.game.map.tileHeight, self.game.map.height - self.image.get_height() - self.game.map.tileHeight)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Armor(Item):

    def __init__(self, itemName, game):
        super().__init__(itemName, game, "art/items/armor/")
        self.protection = random.choice([4.5, 4.0, 4.0, 3.5, 3.5, 3.5, 3.0, 3.0, 3.0, 3.0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5])

class Disc(Item):

    def __init__(self, itemName, game):
        super().__init__(itemName, game, "art/items/discs/")

class Food(Item):

    def __init__(self, itemName, game):
        super().__init__(itemName, game, "art/items/food/")
        self.food = random.choice([9, 8, 7, 7, 6, 6, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2])

class Potion(Item):

    def __init__(self, itemName, game):
        super().__init__(itemName, game, "art/items/potions/")

class Valuable(Item):

    def __init__(self, itemName, game):
        super().__init__(itemName, game, "art/items/valuables/")

class Weapon(Item):

    def __init__(self, itemName, game):
        super().__init__(itemName, game, "art/items/weapons/")
        self.damage = random.choice([15.0, 14.5, 14.0, 13.5, 13.0, 12.5, 12.0, 11.5, 11.0, 11.0, 10.5, 10.5, 10.0, 10.0, 9.5, 9.5, 9.0, 9.0, 8.5, 8.5, 8.0, 8.0, 7.5, 7.5, 7.0, 7.0, 7.0, 6.5, 6.5, 6.5, 6.0, 6.0, 6.0, 5.5, 5.5, 5.5, 5.0, 5.0, 5.0, 4.5, 4.5, 4.5, 4.0, 4.0, 4.0, 3.5, 3.5, 3.5, 3.0, 3.0, 3.0, 3.0, 2.5, 2.5, 2.5, 2.5, 2.0, 2.0, 2.0, 2.0, 1.5, 1.5, 1.5, 1.5, 1.0, 1.0, 1.0, 1.0])
class Misc(Item):

    def __init__(self, itemName, game):
        super().__init__(itemName, game, "art/items/misc/")