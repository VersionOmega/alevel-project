import pygame, random

from classes import enemy

def generateEnemies(game):
    for floorNumber, floor in enumerate(game.dungeon.map):
        for rowNumber, row in enumerate(floor.grid):
            for columnNumber, room in enumerate(row):

                room.numberOfEnemies = random.choice([(floorNumber), (floorNumber), (floorNumber), (floorNumber), (floorNumber), (floorNumber+1), (floorNumber+1), (floorNumber+1), (floorNumber+2)])

                room.enemyDict = {}

                for enemyNumber in range(room.numberOfEnemies):
                    _class = random.choice([1, 2, 3])
                    if _class == 1:
                        room.enemyDict[f"enemy{enemyNumber}"] = enemy.Monster1(20, room, game)
                    elif _class == 2:
                        room.enemyDict[f"enemy{enemyNumber}"] = enemy.Monster2(20, room, game)
                    elif _class == 3:
                        room.enemyDict[f"enemy{enemyNumber}"] = enemy.Monster3(20, room, game)
    
    