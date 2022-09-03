import pygame
import numpy as np
import cv2

from methods import filePath, updatePlayerImage

class Inventory:

    def __init__(self, max, game):
        self.inventoryList = []

        self.max = max
        self.game = game

        self.fistButton = pygame.image.load(str(filePath.path("art/items/clay_ball.png")))

        self.imagePath = filePath.path("art/GUI/inventoryLargePixel.png")
        self.image = pygame.image.load(str(self.imagePath))
        self.image = pygame.transform.scale(self.image, (int(3.5*self.image.get_width()), int(3.5*self.image.get_height())))
        self.image = pygame.transform.scale(self.image, (int((self.game.scaleFactor/57.5)*self.image.get_width()), int((self.game.scaleFactor/57.5)*self.image.get_height())))

        pygame.image.save(self.image, str(filePath.path("art/GUI/modifiedInventoryPixel.png")))


        self.rect = self.image.get_rect()
        #self.rect.x = self.game.windowWidth/2 - self.image.get_width()/2
        #self.rect.y = (game.windowHeight/2)-(self.image.get_height()/2)

        self.createRectDict()

        self.imagePath = filePath.path("art/GUI/inventoryLargeClean.png")
        self.image = pygame.image.load(str(self.imagePath)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(3.5*self.image.get_width()), int(3.5*self.image.get_height()))).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int((self.game.scaleFactor/57.5)*self.image.get_width()), int((self.game.scaleFactor/57.5)*self.image.get_height()))).convert_alpha()

        pygame.image.save(self.image, str(filePath.path("art/GUI/modifiedInventoryClean.png")))

        self.hotImagePath = filePath.path("art/GUI/inventory.png")
        self.hotImage = pygame.image.load(str(self.hotImagePath))
        self.hotImage = pygame.transform.rotate(self.hotImage, 90)
        self.hotImage = pygame.transform.scale(self.hotImage, (int(2*self.hotImage.get_width()), int(2*self.hotImage.get_height())))
        self.hotRect = self.hotImage.get_rect()
        self.hotRect.x = 0
        self.hotRect.y = 0
    
    def createRectDict(self):

        self.rectDict = {}
        for i in range(int(self.max)):
            m = i%9
            d = i//9
            x, y = self.locatePixel((25*(m+1), 0, 0), "TL")[0], self.locatePixel((25*(m+1), 0, 0), "TL")[1]
            temp2 = self.locatePixel((0, 25*(m+1), 0), "BR")
            w = temp2[0] - x
            h = temp2[1] - y

            if d > 0:
                y = self.locatePixel((0, 0, 30*d), "TL")[1]

            self.rectDict[f"rect[{m}x{d}]"] = pygame.Rect(x, y, w, h)
        temp = self.locatePixel((255, 106, 0), "TL")
        temp2 = self.locatePixel((255, 0, 220), "BR")
        x, y = temp[0], temp[1]
        w, h = temp2[0] - x, temp2[1] - y
        self.rectDict["fist"] = pygame.Rect(x, y, w, h)


    def locatePixel(self, RGB, pos):
        color = [RGB[2], RGB[1], RGB[0]]
        im = cv2.imread(str(filePath.path("art/GUI/modifiedInventoryPixel.png")))
        X, Y = np.where(np.all(im==color,axis=2))
        if pos == "TL":
            # Top left corner
            return (min(Y), min(X))
        if pos == "BR":
            return (max(Y), max(X))
    
    def addItem(self, key):
        if len(self.inventoryList) < self.max:

            updatePlayerImage.updatePlayerImage(self.game, self.game.player.currentRoom.itemDict[key])

            self.inventoryList.append(self.game.player.currentRoom.itemDict[key])
            del self.game.player.currentRoom.itemDict[key]
        else:
            pass

    def toggle(self):
        self.visible = not self.visible
    
    def drawHotBar(self, surface):
        surface.blit(self.hotImage, self.hotRect)
        for position, item in enumerate(self.inventoryList):
            if position < 9:
                temp = item.image
                temp = pygame.transform.scale(temp, (int(0.75*temp.get_width()), int(0.75*temp.get_height())))
                surface.blit(temp, (4,(position*40) + 5))



def addItem(self, itemKey):
    item = self.game.player.currentRoom.itemDict[itemKey]
    self.inventoryList.append(item)