import csv, pickle, pygame

from methods import filePath

from classes import item

def save(game):
    reference = []
    for invItem in game.player.inventory.inventoryList:
        if type(invItem) is item.Armor:
            temp = item.Armor(invItem.itemName, invItem.game)

        if type(invItem) is item.Disc:
            temp = item.Disc(invItem.itemName, invItem.game)

        if type(invItem) is item.Food:
            temp = item.Food(invItem.itemName, invItem.game)

        if type(invItem) is item.Potion:
            temp = item.Potion(invItem.itemName, invItem.game)

        if type(invItem) is item.Valuable:
            temp = item.Valuable(invItem.itemName, invItem.game)

        if type(invItem) is item.Weapon:
            temp = item.Weapon(invItem.itemName, invItem.game)

        if type(invItem) is item.Misc:
            temp = item.Misc(invItem.itemName, invItem.game)
        
        temp.displayName = invItem.displayName
        temp.codeName = invItem.codeName
        temp.imagePath = invItem.imagePath
        temp.game = None
        temp.image = None
        temp.rect = invItem.rect
        temp.rect.x = invItem.rect.x
        temp.rect.y = invItem.rect.y

        reference.append(temp)

    inventoryList = pickle.dump(reference, open(str(filePath.path("saves/inventory.p")), "wb"))

def load(game):
    invList = pickle.load(open(str(filePath.path("saves/inventory.p")), "rb"))

    for item in invList:
        item.game = game
        item.image = pygame.transform.scale(pygame.image.load(str(filePath.path(item.imagePath))), (int(pygame.image.load(str(filePath.path(item.imagePath))).get_width()/1.5), int(pygame.image.load(str(filePath.path(item.imagePath))).get_height()/1.5)))

    game.player.inventory.inventoryList = invList


def read():
    with open(filePath.path("saves/save.csv"), "r", newline="") as csvFile:
        reader = csv.reader(csvFile)
        print(reader)

# Need to know how to save an object to a file
