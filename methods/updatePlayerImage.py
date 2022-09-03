from PIL import Image
from methods import filePath
import pygame

def updatePlayerImage(game, item):
    
    """playerImage = Image.open(str(filePath.path("art/player.png")))
    itemImage = Image.open(str(filePath.path(item.imagePath)))

    playerImage.paste(itemImage)

    playerImage.save(str(filePath.path("art/player_modified.png")))"""

    game.player.image = pygame.image.load(str(filePath.path(item.imagePath)))