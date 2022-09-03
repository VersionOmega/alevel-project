# Import the sys and pygame modules
import pygame, sys, pytmx, random, pickle
from screeninfo import get_monitors

# From the classes subfolder, import 
from classes import player, item, miniMap, enemy, keyboardHandler, boss, textBox, camera
# From the methods subfolder, import filePath, updateMap
from methods import filePath, updateMap, generateDungeon, saveGame, generateItems, generateEnemies, updatePlayerImage, generateBosses, generatePlanets

# New class called Game
class Game:

    # Constructor method
    def __init__(self, sf, title, FPS):
        # Make all parameters attributes of the class
        self.scaleFactor = sf
        self.windowWidth = self.scaleFactor*16
        self.windowHeight = self.scaleFactor*16
        self.windowTitle = title
        self.FPS = FPS
        self.defaultTextSize = int(self.scaleFactor/2.5)

        self.numberOfTiles = 15
        self.moveDiagonally = True

        self.loadPrevious = True
        self.running = True

        self.createGame()
        self.load()

        # While the window is open
        while self.running:

            # Keep loop running at certain speed
            self.clock.tick(self.FPS)
            # Loop through the event queue
            for event in pygame.event.get():
                self.event = event
                # If the X button to close the window is pressed
                if event.type == pygame.QUIT:
                    # Close the window
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.healthText = textBox.Box(f"Health: {self.player.health}\nProtection: {self.player.protection}\nDamage Factor: x{round(self.player.calculateProtection(), 1)}\nXP: {self.player.XP}\nInventory: {len(self.player.inventory.inventoryList)}/{self.player.inventory.max}", (0, 0, 0), int((3/4)*self.defaultTextSize), self)

            self.camera.update(self.player)

            if self.scene == "dungeon":
                self.updateDungeon(self.event)
            
            elif self.scene == "inventory":
                self.updateInventory(self.event)

            elif self.scene == "pause":
                self.updatePause(self.event)
            
            elif self.scene == "planet":
                self.updatePlanet(self.event)

            elif self.scene == "fight":
                self.updateFight(self.event)
            
            elif self.scene == "gameover":
                self.updateGameOver(self.event)
            
            elif self.scene == "win":
                self.updateWin(self.event)
            
            elif self.scene == "select":
                self.updateSelect(self.event)
            
            elif self.scene == "welcome":
                self.updateWelcome(self.event)
            
            self.statusText.draw(self.screen, (0, 0))
                
            # Update the window
            pygame.display.update()

            self.now = pygame.time.get_ticks()
            

    def createGame(self):
        
        # Initialise pygame and pygame's mixer (for audio)
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        # Create a new pygame window, with (Width, Height) of (self.windowWidth, self.windowHeight) and 
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE|pygame.DOUBLEBUF)

        # Set the title of the pygame window
        pygame.display.set_caption(self.windowTitle)
        
        # Create a pygame clock
        self.clock = pygame.time.Clock()

        self.scene = "welcome"

        self.gameOver = False

    def load(self):
        
        #self.dungeon = pickle.load(open("dungeonObject.p", "rb"))

        self.dungeon = generateDungeon.Dungeon(4, 11, 15)

        updateMap.update(self, "maps/31x31/BLA.tmx")

        self.player = player.Player((255,0,0), 64,64, self)
        #self.player.inventory.inventoryList = pickle.load(open("inventoryObject.p", "rb"))

        self.player.currentFloor = self.dungeon.map[0]
        self.player.currentFloor.floorNumber = 0
        self.player.currentRoom = self.player.currentFloor.grid[random.randint(self.player.currentFloor.min, self.player.currentFloor.max)][random.randint(self.player.currentFloor.min, self.player.currentFloor.max)]
        while self.player.currentRoom.name in ["SDN", "SDE", "SDS", "SDW", "BLA"]:
            self.player.currentRoom = self.player.currentFloor.grid[random.randint(self.player.currentFloor.min, self.player.currentFloor.max)][random.randint(self.player.currentFloor.min, self.player.currentFloor.max)]
    
        
        # Create a new

        self.backgroundImage = pygame.image.load(str(filePath.path("art/background.png")))
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.windowWidth, self.windowHeight))

        self.miniMap = miniMap.MiniMap(self)

        self.fightTurn = 0
        
        self.maxItems = 25
        generateItems.generateItems(self)

        generateEnemies.generateEnemies(self)

        generateBosses.generateBosses(self)

        generatePlanets.generatePlanets(self)

        updateMap.update(self, self.player.currentRoom.fileName)

        self.camera = camera.Camera(self.map.width, self.map.height, self)

        self.statusText = textBox.Box("", (0, 0, 0), self.defaultTextSize, self)
        self.healthText = textBox.Box(f"Health: {self.player.health}\nProtection: {self.player.protection}\nDamage Factor: x{round(self.player.calculateProtection(), 1)}\nXP: {self.player.XP}\nInventory: {len(self.player.inventory.inventoryList)}/{self.player.inventory.max}", (0, 0, 0), int((3/4)*self.defaultTextSize), self)
        self.welcomeText = textBox.Box(f"Welcome.\n\n\n* Press 'L' to load inventory\n\n\n* Press 'P' at any time to pause the game\n\n\n* Use WASD or the arrow keys to move around\n\n\n* Press 'ENTER' to continue...", (255, 255, 255), int(self.defaultTextSize*1.25), self)
        self.pauseText = textBox.Box(f"* Press 'ESC' to return\n\n\n* Press 'E' in-game to open your inventory\n\n\n* Press 'S' now to save your inventory", (0, 0, 0), self.defaultTextSize, self)
        
    def updateFight(self, event):

        if self.statusText.timeDelay(2500):
            self.statusText = textBox.Box("", (0, 0, 0), self.defaultTextSize, self)

        self.enemyText = textBox.Box(f"Health: {self.player.currentEnemy.health}\nDamage: {self.player.currentEnemy.damage}", (0, 0, 0), int((3/4)*self.defaultTextSize), self)

        self.screen.fill((167, 167, 167))

        temp = self.player.image
        temp = pygame.transform.scale(temp, (int((self.scaleFactor/20)*temp.get_width()), int((self.scaleFactor/20)*temp.get_height())))
        self.screen.blit(temp, ((temp.get_width())/2, (self.windowHeight - (self.healthText.image.get_height() + 3*temp.get_height()/2))))

        temp2 = self.player.currentEnemy.image
        temp2 = pygame.transform.scale(temp2, (int((self.scaleFactor/32.5)*temp2.get_width()), int((self.scaleFactor/32.5)*temp2.get_height())))
        self.screen.blit(temp2, (self.windowWidth - (8*temp2.get_width()/5), temp2.get_height()/2))

        if self.fightTurn % 2 == 0:
            # Player's turn
            try:
                if event.text == "e" or event.unicode == "e":
                    self.previousScene = self.scene
                    self.scene = "inventory"
            except:
                pass
        else:
            
            if self.statusText.timeDelay(2000):
                damage = round(self.player.calculateProtection()*(self.player.currentEnemy.damage), 1)
                self.statusText = textBox.Box(f"{self.player.currentEnemy.name} attacked you and dealt {damage} damage!", (138, 8, 17), self.defaultTextSize, self)
                self.player.health = round(self.player.health - damage, 1)
                self.fightTurn += 1
        
        
        if self.player.currentEnemy.health <= 0:
            self.previousScene = self.scene
            self.scene = "dungeon"
            del self.player.currentRoom.enemyDict[self.player.currentEnemyKey]
            self.fightTurn = 0
            self.player.protection = 1
            exp = int((2*(self.player.health)/19)*self.player.currentEnemy.damage)
            self.player.XP += exp
            self.statusText = textBox.Box(f"You defeated {self.player.currentEnemy.name}! You received {exp} XP!", (28, 128, 30), self.defaultTextSize, self)

            if self.player.currentFloor.floorNumber == self.dungeon.numberOfFloors - 1 and self.player.currentEnemyKey == "boss0":
                self.scene = "win"

        if self.player.health <= 0:
            self.previousScene = self.scene
            self.scene = "gameover"
        
        self.healthText.draw(self.screen, (0, self.windowHeight - self.healthText.image.get_height()))
        self.enemyText.draw(self.screen, (self.windowWidth - self.enemyText.image.get_width(), (2*temp2.get_height())))
    
    def updateInventory(self, event):
        if self.statusText.timeDelay(2500):
            self.statusText = textBox.Box("", (0, 0, 0), self.defaultTextSize, self)

        self.screen.fill((167,167,167))
        x, y = int(self.windowWidth/2 - self.player.inventory.image.get_width()/2), int(self.windowHeight/2 - self.player.inventory.image.get_height()/2)
        self.screen.blit(self.player.inventory.image, (x, y))
        pos = pygame.mouse.get_pos()
        pos = (pos[0] - x, pos[1] - y)
        rec = self.player.inventory.image.get_rect()

        for key, rec in self.player.inventory.rectDict.items():
            if key == "fist":
                pygame.draw.rect(self.player.inventory.image, (198, 198, 198), rec)
            else:
                pygame.draw.rect(self.player.inventory.image, (139, 139, 139), rec)

        for position, gameItem in enumerate(self.player.inventory.inventoryList):

            m, d = position%9, position//9
            img = gameItem.image
            rec = self.player.inventory.rectDict[f"rect[{m}x{d}]"]
            
            self.player.inventory.image.blit(pygame.transform.scale(img, (rec.w, rec.h)), rec)

            if rec.collidepoint(pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Use item

                    if type(gameItem) is item.Weapon and self.previousScene == "fight":
                        # The player is in a fight, and has clicked on a weapon (i.e. do damage to enemy)
                        self.player.currentEnemy.health -= gameItem.damage
                        self.scene = self.previousScene
                        self.fightTurn += 1
                        self.statusText = textBox.Box(f"You used a {gameItem.displayName} against {self.player.currentEnemy.name} and did {gameItem.damage} damage!", (28, 128, 30), self.defaultTextSize, self)
                    
                    if type(gameItem) is item.Food:
                        self.player.setHealth(gameItem.food)
                        self.player.inventory.inventoryList.remove(gameItem)
                        self.scene = self.previousScene
                        if self.previousScene == "fight":
                            self.fightTurn += 1
                            self.statusText = textBox.Box(f"You ate a {gameItem.displayName} and gained {gameItem.food} health!", (28, 128, 30), self.defaultTextSize, self)
                        else:
                            self.statusText = textBox.Box(f"You ate a {gameItem.displayName} and gained {gameItem.food} health!", (63, 138, 132), self.defaultTextSize, self)
                    
                    if type(gameItem) is item.Armor and self.previousScene == "fight":
                        self.player.protection += gameItem.protection
                        self.player.inventory.inventoryList.remove(gameItem)
                        self.scene = self.previousScene
                        self.fightTurn += 1
                        self.statusText = textBox.Box(f"You equipped some {gameItem.displayName} and increased your protection by {gameItem.protection}!", (28, 128, 30), self.defaultTextSize, self)
                    
                    if type(gameItem) is item.Armor and self.previousScene == "dungeon":
                        self.scene = self.previousScene
                        self.statusText = textBox.Box(f"You examine the {gameItem.displayName} and discover it has {gameItem.protection} protection!", (63, 138, 132), self.defaultTextSize, self)
                    
                    if type(gameItem) is item.Weapon and self.previousScene == "dungeon":
                        self.scene = self.previousScene
                        self.statusText = textBox.Box(f"You examine the {gameItem.displayName} and discover it deals {gameItem.damage} damage!", (63, 138, 132), self.defaultTextSize, self)
                

                # UNCOMMENT THIS TO ENABLE DROPPING
                else:
                    try:
                        if event.text == "q" or event.unicode == "q":
                            self.player.inventory.inventoryList.remove(gameItem)
                            self.player.currentRoom.itemDict[f"item{len(self.player.currentRoom.itemDict)+1}"] = gameItem

                            self.player.currentRoom.itemDict[f"item{len(self.player.currentRoom.itemDict)}"].rect.x = random.randint(int(self.windowWidth/self.numberOfTiles), int(self.windowWidth-gameItem.image.get_width()-(self.windowWidth/self.numberOfTiles)))
                            self.player.currentRoom.itemDict[f"item{len(self.player.currentRoom.itemDict)}"].rect.y = random.randint(int(self.windowHeight/self.numberOfTiles), int(self.windowHeight-gameItem.image.get_height()-(self.windowHeight/self.numberOfTiles)))

                            self.scene = "dungeon"
                            self.statusText = textBox.Box(f"You dropped your {gameItem.displayName}!", (63, 138, 132), self.defaultTextSize, self)
                    
                    except:
                        pass
        
        if self.previousScene == "fight":
            rec = self.player.inventory.rectDict["fist"]
            self.player.inventory.image.blit(pygame.transform.scale(self.player.inventory.fistButton, (rec.w, rec.h)), rec)

            if rec.collidepoint(pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.currentEnemy.health -= 1
                    self.scene = self.previousScene
                    self.fightTurn += 1
                    self.statusText = textBox.Box(f"You used your fists against {self.player.currentEnemy.name} and did 1 damage!", (0, 0, 0), self.defaultTextSize, self)

        tempReference = self.player.image
        tempReference = pygame.transform.scale(tempReference, (int(2.3*tempReference.get_width()), int(2.3*tempReference.get_height())))
        self.player.inventory.image.blit(tempReference, (0, 0))

        try:
            if event.key == 27:
                self.scene = self.previousScene
        except:
            pass

    def updateDungeon(self, event):
        
        self.screen.fill((0, 0, 0))
        self.welcomeText = textBox.Box(f"Welcome.\n\n\n* Press 'L' to load inventory\n\n\n* Press 'P' at any time to pause the game\n\n\n* Use WASD or the arrow keys to move around\n\n\n* Press 'ENTER' to continue...", (255, 255, 255), 30, self)
        self.pauseText = textBox.Box(f"* Press 'ESC' to return\n\n\n* Press 'E' in-game to open your inventory\n\n\n* Press 'S' now to save your inventory", (0, 0, 0), self.defaultTextSize, self)

        if self.statusText.timeDelay(3000):
            self.statusText = textBox.Box(f"", (0, 0, 0), self.defaultTextSize, self)

        pressed = pygame.key.get_pressed()

        for layer in self.map.tmxData.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if pygame.Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height)).colliderect(self.player.rect):
                        # Collision with a collision box
                        self.player.collide(obj, self.player.movement)
                        self.player.movement = 'rest'

        self.screen.blit(self.mapImage, (self.camera.viewRect.x,self.camera.viewRect.y))
        self.player.update(event)
        self.player.draw(self.screen, self.camera.apply(self.player))

        for gameItem in self.player.inventory.inventoryList:
            if gameItem.displayName == "Map":
                self.miniMap.draw(self.screen)
            

        for key, gameItem in self.player.currentRoom.itemDict.items():
            self.screen.blit(gameItem.image, self.camera.apply(gameItem))
            
        
        for key in list(self.player.currentRoom.itemDict):
            if self.player.currentRoom.itemDict[key].rect.colliderect(self.player.rect):
                if event.type == pygame.MOUSEBUTTONUP:
                    self.player.inventory.addItem(key)
            
             
        for key, gameEnemy in self.player.currentRoom.enemyDict.items():
            self.screen.blit(gameEnemy.image, self.camera.apply(gameEnemy))
            gameEnemy.move()
            if gameEnemy.rect.colliderect(self.player.rect):
                self.previousScene = self.scene
                self.player.currentEnemy = gameEnemy
                self.player.currentEnemyKey = key
                self.scene = "fight"
                self.statusText = textBox.Box(f"Press 'E' to open your inventory and select a weapon!", (63, 138, 132), self.defaultTextSize, self)

        try:
            if event.text == "p" or event.unicode == "p":
                self.previousScene = self.scene
                self.scene = "pause"
        except:
            pass

        try:
            if event.text == "e" or event.unicode == "e":
                self.previousScene = self.scene
                self.scene = "inventory"
                self.statusText = textBox.Box(f"Press 'Q' while hovering over an item to drop it!", (63, 138, 132), self.defaultTextSize, self)
            
        except:
            pass
            
        self.healthText.draw(self.screen, (0, self.windowHeight - self.healthText.image.get_height()))
        self.planetText.draw(self.screen, (self.windowWidth-self.planetText.image.get_width(), self.windowHeight-self.planetText.image.get_height()))
        if self.planetText.timeDelay(5000):
            self.planetText = textBox.Box("", (0, 0, 0), self.defaultTextSize, self)
    
    def updatePlanet(self, event):
        self.screen.blit(self.backgroundImage, (0,0))

        for planetName, planetObject in self.planetDict.items():
            self.screen.blit(planetObject.image, planetObject.rect)

            pos = pygame.mouse.get_pos()

            if planetObject.rect.collidepoint(pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selectedPlanet = planetObject
                    self.previousScene = self.scene
                    self.scene = "select"
        try:
            if event.text == "p" or event.unicode == "p":
                self.previousScene = self.scene
                self.scene = "pause"
        except:
            pass

    def updateGameOver(self, event):
        self.screen.fill((0,0,0))
        self.gameOverText = textBox.Box(f"GAME OVER\n\n\nScore: {self.player.XP} XP", (255, 0, 0), 48, self)
        self.statusText = textBox.Box("", (0, 0, 0), self.defaultTextSize, self)
        if not self.gameOver:
            sound = pygame.mixer.Sound("gameover.mp3")
            sound.play()
            self.gameOver = True
        self.gameOverText.draw(self.screen, (self.windowWidth/2 - self.gameOverText.image.get_width()/2, self.windowHeight/2 - self.gameOverText.image.get_height()/2))
    
    def updateWin(self, event):
        self.screen.fill((0,0,0))
        self.winText = textBox.Box(f"YOU WIN\n\n\nScore: {self.player.XP} XP", (0, 255, 0), 48, self)
        self.statusText = textBox.Box("", (0, 0, 0), self.defaultTextSize, self)
        self.winText.draw(self.screen, (self.windowWidth/2 - self.gameOverText.image.get_width()/2, self.windowHeight/2 - self.gameOverText.image.get_height()/2))

    def updatePause(self, event):
        self.screen.fill((167, 167, 167))
            
        self.pauseText.draw(self.screen, (0, 100))

        try:
            if event.key == 27:
                self.scene = self.previousScene
        except:
            pass

        try:
            if event.text == "s" or event.unicode == "s":
                saveGame.save(self)
                self.pauseText = textBox.Box(f"* Press 'ESC' to return\n\n\n* Press 'E' in-game to open your inventory\n\n\n* INVENTORY SAVED!", (0, 0, 0), self.defaultTextSize, self)
        except:
            pass
    
    def updateWelcome(self, event):
        self.screen.fill((0, 0, 0))
        self.welcomeText.draw(self.screen, (0, 100))

        try:
            
            if event.key == 13:
                self.previousScene = self.scene
                self.scene = "planet"
        except:
            pass

        try:
            
            if event.text == "l" or event.unicode == "l":
                saveGame.load(self)
                self.welcomeText = textBox.Box(f"Welcome.\n\n\n* INVENTORY LOADED!\n\n\n* Press 'P' at any time to pause the game\n\n\n* Use WASD or the arrow keys to move around\n\n\n* Press 'ENTER' to continue...", (255, 255, 255), self.welcomeText.size, self)
        except:
            pass
        
    def updateSelect(self, event):
        self.screen.blit(self.backgroundImage, (0,0))

        self.planetText = textBox.Box(f"Name: {self.selectedPlanet.name}\n\n\n\nPress 'ENTER' to play\n\nPress 'BACK' to return", (255, 255, 255), self.defaultTextSize, self)
        self.planetText.draw(self.screen, (0, self.windowHeight-(3*self.planetText.image.get_height())/2))

        temp = self.selectedPlanet.image
        temp = pygame.transform.scale(temp, (int(temp.get_width()/0.5), int(temp.get_height()/0.5)))
        self.screen.blit(temp, (self.windowWidth/2 - self.selectedPlanet.image.get_width()/2, (self.windowHeight)/5))

        try:
            if event.key == 8:
                self.scene = "planet"
        except:
            pass
        try:
            if event.key == 13:
                self.previousScene = self.scene
                self.scene = "dungeon"
                self.planetText = textBox.Box(f"", (0, 0, 0), self.defaultTextSize, self)
        except:
            pass
        try:
            if event.text == "p" or event.unicode == "p":
                self.previousScene = self.scene
                self.scene = "pause"
        except:
            pass

import tkinter

if __name__ == "__main__":
    # Create a new Game object called game
    for m in get_monitors():
        h = m.height
    game = Game(int(h/24), "Test", 360)


"""
FIX ITEM AND ENEMY GENERATION
DONE!
"""