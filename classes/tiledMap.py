# This code was taken primarily from the KidsCanCode Youtube channel
# as well as the Pygame documentation, see the references below:
# https://www.youtube.com/watch?v=Mr5l4U9S4kI
# https://www.pygame.org/project-Tiled+TMX+Loader-2036-.html

import pygame, pytmx

class Map:

    def __init__(self, file):
        self.tmxData = pytmx.TiledMap(file)
        self.width = self.tmxData.width * self.tmxData.tilewidth
        self.height = self.tmxData.height * self.tmxData.tileheight
        self.tileWidth = self.tmxData.tilewidth
        self.tileHeight = self.tmxData.tileheight
        self.tmxDataOld = pytmx.load_pygame(file)
    
    def render(self, surface):
        self.tileImage = self.tmxDataOld.get_tile_image_by_gid
        for layer in self.tmxData.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tileImage(gid)
                    if tile:
                        surface.blit(tile, (x*self.tmxData.tilewidth, y*self.tmxData.tileheight))
    def create(self):
        terrain = pygame.Surface((self.width, self.height), pygame.HWSURFACE|pygame.DOUBLEBUF)
        self.render(terrain)
        return terrain

