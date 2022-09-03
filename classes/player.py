import pygame, math

from methods import updateMap, filePath

from classes import inventory, miniMap

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, game):
        super().__init__()

        self.imagePath = filePath.path("art/DEMOPLAYER.png")
        self.image = pygame.image.load(str(self.imagePath))
        self.rect = self.image.get_rect()

        
        self.maxHealth = 30
        self.health = self.maxHealth

        self.game = game

        self.movementSpeed = 1.5

        self.XP = 0

        self.movement = 'rest'

        self.protection = 1

        self.inventory = inventory.Inventory(27, self.game)
    
    def setHealth(self, increment):
        if self.health + increment >= 30:
            self.health = 30
        else:
            self.health += increment


    def update(self, event):


        if self.game.moveDiagonally:
            if event != None:

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_w] or pressed[pygame.K_UP]:
                    if self.rect.y >= 2*self.movementSpeed:
                        self.rect.y -= 2*self.movementSpeed
                        self.movement = "up"

                if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
                    if self.rect.y <= self.game.map.height - self.rect.height - (2*self.movementSpeed):
                        self.rect.y += 2*self.movementSpeed
                        self.movement = "down"

                if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
                    if self.rect.x >= 2*self.movementSpeed:
                        self.rect.x -= 2*self.movementSpeed
                        self.movement = "left"

                if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
                    if self.rect.x <= self.game.map.width - self.rect.width - (2*self.movementSpeed):
                        self.rect.x += 2*self.movementSpeed
                        self.movement = "right"
        else:
            if event != None:

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_w] or pressed[pygame.K_UP]:
                    self.rect.x += 0
                    self.rect.y += -2*self.movementSpeed
                    self.movement = "up"

                elif pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
                    self.rect.x += 0
                    self.rect.y += 2*self.movementSpeed
                    self.movement = "down"

                elif pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
                    self.rect.x += -2*self.movementSpeed
                    self.rect.y += 0
                    self.movement = "left"
                    
                elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
                    self.rect.x += 2*self.movementSpeed
                    self.rect.y += 0
                    self.movement = "right"

    def draw(self, display, position):
        display.blit(self.image, position)
    
    def calculateProtection(self):
        if self.protection < 2:
            return 1
        else:
            #return math.e**(-0.1*self.protection)+(1-math.e**(-0.2))
            return -1*(1/3)*math.log(self.protection)+(1+((1/3)*math.log(2)))

    def collide(self, obj, motion):

        if obj.name == "NORTH":
            # Player wants to go to the room above
            self.currentRoom = self.currentFloor.grid[self.currentRoom.gridIndex[0]-1][self.currentRoom.gridIndex[1]]
            # Centres the player in the X direction
            self.rect.x = self.game.map.width/2 - self.image.get_width()/2
            # Places the player 1 doorway height (self.game.map.tileHeight) and 1 player height (self.image.get_height()) from window height (self.game.map.height)
            self.rect.y = self.game.map.height - (self.game.map.tileHeight + self.image.get_height())

        if obj.name == "EAST":
            # Player wants to go to the room to the right
            self.currentRoom = self.currentFloor.grid[self.currentRoom.gridIndex[0]][self.currentRoom.gridIndex[1]+1]
            # Places the player 1 doorway width away
            self.rect.x = self.game.map.tileWidth
            # Centres the player in the Y direction
            self.rect.y = self.game.map.height/2 - self.image.get_height()/2

        if obj.name == "SOUTH":
            # Player wants to go to the room below
            self.currentRoom = self.currentFloor.grid[self.currentRoom.gridIndex[0]+1][self.currentRoom.gridIndex[1]]
            # Centres the player in the X direction
            self.rect.x = self.game.map.width/2 - self.image.get_width()/2
            # Places the player 1 doorway height away
            self.rect.y = self.game.map.tileHeight

        if obj.name == "WEST":
            # Player wants to go to the room to the left
            self.currentRoom = self.currentFloor.grid[self.currentRoom.gridIndex[0]][self.currentRoom.gridIndex[1]-1]
            # Places the player 1 doorway width (self.game.map.tileWidth) and 1 player width (self.image.get_width()) from window width (self.game.map.width)
            self.rect.x = self.game.map.width - (self.image.get_width() + self.game.map.tileWidth)
            # Centres the player in the Y direction
            self.rect.y = self.game.map.height/2 - self.image.get_height()/2

        if obj.name == "STAIRDOWN":
            # When moving down a floor, first ask the player to confirm as they cant move back up
            # Then we need to change the current floor
            # Update the mini map
            if self.currentRoom.enemyDict == {}:
                self.currentFloor.floorNumber += 1
                temp = self.currentFloor.floorNumber
                self.currentFloor = self.game.dungeon.map[temp]
                self.currentFloor.floorNumber = temp
                self.currentRoom = self.currentFloor.grid[self.currentRoom.gridIndex[0]][self.currentRoom.gridIndex[1]]
                self.game.miniMap = miniMap.MiniMap(self.game)
            else:
                pass

        updateMap.update(self.game, filePath.path(self.currentRoom.fileName))