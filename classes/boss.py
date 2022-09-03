import pygame
from classes import enemy

class Boss(enemy.Enemy):

    def __init__(self, name, health, room, game):
        super().__init__(name, health, room, game)
        self.image.fill((255, 0, 0))