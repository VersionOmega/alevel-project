import pygame, random

class Enemy(pygame.sprite.Sprite):

    enemyGroup = pygame.sprite.Group()

    def __init__(self, health, room, game):
        super().__init__()

        self.game = game

        self.stubbornness = game.FPS*(random.randint(1, 5))
        self.activity = 0

        self.fitnessLimit = game.FPS*(random.randint(1,8))
        self.laziness = 0

        self.moveDirectionX = None
        self.moveDirectionY = None

        self.damage = 2
        
        self.name = random.choice(['Stoneteeth', 'Hellhag', 'Sorrowgolem', 'Stoneteeth', 'Sorrowgolem', 'Stoneseeker', 'Aromatic Screamer', 'Dangerous Corpse', 'Awful Anomaly', 'Awful Anomaly', 'Mad Moon Tiger', 'Painted Cavern Vermin', 'Obsidian Boulder Bat', 'Obsidian Boulder Bat', 'Thornpod', 'Poisonteeth', 'Netherfoot', 'Cloudsnake', 'Reckless Abortion', 'Outlandish Abnormality', 'Outlandish Abnormality', 'Mean Gnoll', 'Black-Eyed Cave Rhino', 'Jade Venom Behemoth', 'Jade Venom Behemoth', 'Sapphire Dire Leviathan', 'Sapphire Dire Leviathan', 'Infernomirage', 'Plaguescreamer', 'Stoneghoul', 'Spiteling', 'Bewitched Brute', 'Calm Monster', 'Nasty Wraith', 'Taloned Jester Dragon', 'Taloned Demon Spider', 'Elusive Cavern Jackal', 'Barbcreep', 'Cinderserpent', 'Ashbug', 'Moldtooth', 'Cold Hag', 'Hollow Eyes', 'Bruised Tree', 'Golden Moon Dog', 'Titanic Vampire Critter', 'Tusked Horror Anaconda', 'Smogbeing', 'Cloudmonster', 'Thundermorph', 'Gloomthing', 'Disgusting Face', 'Forsaken Vision', 'Electric Behemoth', 'Crimson Moon Bear', 'Black-Striped Razorback Lion', 'Stalking Horror Sheep', 'Fogwing', 'Decayfiend', 'Trancebeing', 'Glowstrike', 'Icy Mutant', 'Disgusting Freak', 'Electric Creature', 'Painted Mountain Behemoth', 'Taloned Tomb Freak', 'Silver Storm Warthog', 'Glowmutant', 'Dustface', 'Voodootree', 'Spectralstrike', 'Dark Deviation', 'Undead Eyes', 'Muted Howler', 'Fiery Corpse Leviathan', 'Patriarch Nightmare Phoenix', 'Golden Razorback Jackal'])
        self.health = health
        self.image = pygame.Surface([96, 96])
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(self.game.map.tileWidth, self.game.map.width - self.image.get_width() - self.game.map.tileWidth)
        self.rect.y = random.randint(self.game.map.tileHeight, self.game.map.height - self.image.get_height() - self.game.map.tileHeight)

        self.room = room

        self.movementSpeed = 2

        self.__class__.enemyGroup.add(self)
    
    def move(self):
        self.activity += 1


        if self.activity == self.stubbornness and self.laziness <= self.fitnessLimit:
            self.moveDirectionX = random.choice(["E",None,"W"])
            self.moveDirectionY = random.choice(["S",None,"N"])

        if self.activity >= self.stubbornness and self.laziness <= self.fitnessLimit:
            self.laziness += 1
            if self.laziness > self.fitnessLimit:
                self.activity = 0
                self.laziness = 0
            else:
                if self.moveDirectionX == "W":
                    if self.moveDirectionY == "N":
                        # Moving NW
                        if self.rect.x > self.game.map.tileWidth and self.rect.y > self.game.map.tileWidth:
                            self.rect.move_ip(self.movementSpeed*-1, self.movementSpeed*-1)
                        else:
                            pass
                    elif self.moveDirectionY == "S":
                        # Moving SW
                        if self.rect.x > self.game.map.tileWidth and self.rect.y + self.image.get_height() < self.game.map.height - self.game.map.tileWidth:
                            self.rect.move_ip(self.movementSpeed*-1, self.movementSpeed*1)
                        else:
                            pass
                    else:
                        # Moving W
                        if self.rect.x > self.game.map.tileWidth:
                            self.rect.move_ip(self.movementSpeed*-1, self.movementSpeed*0)
                        else:
                            pass

                elif self.moveDirectionX == "E":
                    if self.moveDirectionY == "N":
                        # Moving NE
                        if self.rect.x + self.image.get_width() < self.game.map.width - self.game.map.tileWidth and self.rect.y > self.game.map.tileWidth:
                            self.rect.move_ip(self.movementSpeed*1, self.movementSpeed*-1)
                        else:
                            pass
                    elif self.moveDirectionY == "S":
                        # Moving SE
                        if self.rect.x + self.image.get_width() < self.game.map.width - self.game.map.tileWidth and self.rect.y + self.image.get_height() < self.game.map.height - self.game.map.tileWidth:
                            self.rect.move_ip(self.movementSpeed*1, self.movementSpeed*1)
                        else:
                            pass
                    else:
                        # Moving E
                        if self.rect.x + self.image.get_width() < self.game.map.width - self.game.map.tileWidth:
                            self.rect.move_ip(self.movementSpeed*1,self.movementSpeed*0)
                        else:
                            pass
                else:
                    if self.moveDirectionY == "S":
                        # Moving S
                        if self.rect.y + self.image.get_height() < self.game.map.height - self.game.map.tileWidth:
                            self.rect.move_ip(self.movementSpeed*0,self.movementSpeed*1) 
                    elif self.moveDirectionY == "N":
                        # Moving N
                        if self.rect.y > self.game.map.tileWidth:
                            self.rect.move_ip(self.movementSpeed*0,self.movementSpeed*-1)
                    else:
                        # Not moving
                        pass
            
        
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
class Monster1(Enemy):

    def __init__(self, health, room, game):
        super().__init__(health, room, game)
        self.health = health
        self.image = pygame.Surface([96, 96])
        self.image.fill((0,255,0))
        self.movementSpeed = 5
        self.damage = 1
        self.health = 10

class Monster2(Enemy):

    def __init__(self, health, room, game):
        super().__init__(health, room, game)
        self.health = health
        self.image = pygame.Surface([96, 96])
        self.image.fill((255,0,255))
        self.movementSpeed = 1
        self.damage = 5
        self.health = 25

class Monster3(Enemy):

    def __init__(self, health, room, game):
        super().__init__(health, room, game)
        self.health = health
        self.image = pygame.Surface([96, 96])
        self.image.fill((0,0,255))

class Boss(Enemy):

    def __init__(self, health, room, game):
        super().__init__(health, room, game)
        self.health = health
        self.image = pygame.Surface([118, 118])
        self.image.fill((128, 0, 128))
        self.damage = 2.5*(health/50)+2.5