import pygame, random, os

from classes import item

from methods import filePath

def generateItems(game):
    randomItemNumberList = []
    total = 1
    for i in reversed(range(game.maxItems+1)):
        for j in range(int(total)):
            randomItemNumberList.append(int(i))
        total += 0.425

    # Loops through every room in every floor of the dungeon
    for floorNumber, floor in enumerate(game.dungeon.map):
        for rowNumber, row in enumerate(floor.grid):
            for columnNumber, room in enumerate(row):
                room.numberOfItems = random.choice(randomItemNumberList)
                room.itemDict = {}
                for itemNumber in range(room.numberOfItems):
                    #category = random.choice(["armor", "discs", "food", "potions", "valuables", "weapons"])
                    category = random.choice(["armor", "food", "weapons"])
                    imageList = [item for item in os.listdir(str(filePath.path(f"art/items/{category}"))) if item[-4:]==".png" and item[0] != "."]
                    choice = random.choice(imageList)
                    if category == "armor":
                        room.itemDict[f"item{itemNumber}"] = item.Armor(choice, game)
                    elif category == "discs":
                        room.itemDict[f"item{itemNumber}"] = item.Disc(choice, game)
                    elif category == "food":
                        room.itemDict[f"item{itemNumber}"] = item.Food(choice, game)
                    elif category == "potions":
                        room.itemDict[f"item{itemNumber}"] = item.Potion(choice, game)
                    elif category == "valuables":
                        room.itemDict[f"item{itemNumber}"] = item.Valuable(choice, game)
                    elif category == "weapons":
                        room.itemDict[f"item{itemNumber}"] = item.Weapon(choice, game)

    # To make sure the map generates on X floor, set random.randint(X,X)
    # For a random floor, set random.randint(0, game.dungeon.numberOfFloors-1)
    floor = random.randint(0, 0)
    row = random.choice(game.dungeon.map[floor].grid)
    room = random.choice(row)

    room = game.dungeon.map[0].grid[0][0]

    room.itemDict["item0"] = item.Misc("map.png", game)

    