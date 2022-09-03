# Import the 'pygame' module
import pygame
# Import the 'random' module
import random

from classes import planet

def generatePlanets(game):
    game.planetDict = {}
    # Loop 2 to 20 times
    for i in range(random.randint(2,15)):
        # Format Planet{i} -> Planet0 and assign the value to the variable 'key'
        key = f"Planet{i}"
        # Assign the instance of Planet to the variable 'value
        value = planet.Planet(game)

        rectList = [i.rect for j, i in game.planetDict.items()]
        
        finished = False

        while not finished:

            for rect in rectList:
                if value.rect.colliderect(rect):
                    value = planet.Planet(game)
                    break
            finished = True
                        
        game.planetDict[key] = value