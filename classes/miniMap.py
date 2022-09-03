from PIL import Image
from methods import filePath
import pygame

class MiniMap:

    def __init__(self, game):
        self.game = game
        self.visible = True
        img = Image.new("RGB", (960*self.game.dungeon.floorRadius,960*self.game.dungeon.floorRadius), (255,0,0))
        for y, row in enumerate(self.game.player.currentFloor.grid):
            for x, room in enumerate(row):
                img2 = Image.open(filePath.path(room.image), "r")
                img.paste(img2, (x*960,y*960))
        img = img.resize((192,192))
        img.save(filePath.path("art/map.png"))

        self.miniMapImage = pygame.image.load(str(filePath.path("art/map.png")))
        self.x = self.game.windowWidth-self.miniMapImage.get_width()
        self.y = 0
    
    def toggle(self):
        self.visible = not self.visible

    def draw(self, surface):
        if self.visible:
            surface.blit(self.miniMapImage, (self.x, self.y))