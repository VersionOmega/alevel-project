# From the classes subfolder, import tiledMap
from classes import tiledMap


def update(game, map):
    # Create a new Tiled Map object
    game.map = tiledMap.Map(map)
    # Create a surface from the map object
    game.mapImage = game.map.create()
