import random

class Room:

    roomList = []
    opposites = {
        "north":"south",
        "south":"north",
        "east":"west",
        "west":"east"
    }
    def __init__(self, template, y, x, mapSize):
        self.template = template
        self.exit = self.template[0]
        self.name = self.template[1]
        self.fileName = f"maps/{mapSize}x{mapSize}/{self.name}.tmx"
        self.image = self.template[3]
        self.y = y
        self.x = x
        self.gridIndex = (self.y, self.x)

        self.__class__.roomList.append(self)

class RoomBlueprint:

    def __init__(self, exits, name, fileName, image):
        self.info = (
            exits,
            name,
            fileName,
            image
        )

CNW = RoomBlueprint(
    {
        "north":False,
        "east":True,
        "south":True,
        "west":False
    }, "CNW", "maps/31x31/CNW.tmx", "art/CNW.png"
)
NOR = RoomBlueprint(
    {
        "north":False,
        "east":True,
        "south":True,
        "west":True
    }, "NOR", "maps/31x31/NOR.tmx", "art/NOR.png"
)
CNE = RoomBlueprint(
    {
        "north":False,
        "east":False,
        "south":True,
        "west":True
    }, "CNE", "maps/31x31/CNE.tmx", "art/CNE.png"
)
WES = RoomBlueprint(
    {
        "north":True,
        "east":True,
        "south":True,
        "west":False
    }, "WES", "maps/31x31/WES.tmx", "art/WES.png"
)
ORI = RoomBlueprint(
    {
        "north":True,
        "east":True,
        "south":True,
        "west":True
    },  "ORI", "maps/31x31/ORI.tmx", "art/ORI.png"
)
EAS = RoomBlueprint(
    {
        "north":True,
        "east":False,
        "south":True,
        "west":True
    }, "EAS", "maps/31x31/EAS.tmx", "art/EAS.png"
)
CSW = RoomBlueprint(
    {
        "north":True,
        "east":True,
        "south":False,
        "west":False
    }, "CSW", "maps/31x31/CSW.tmx", "art/CSW.png"
)
SOU = RoomBlueprint(
    {
        "north":True,
        "east":True,
        "south":False,
        "west":True
    }, "SOU", "maps/31x31/SOU.tmx", "art/SOU.png"
)
CSE = RoomBlueprint(
    {
        "north":True,
        "east":False,
        "south":False,
        "west":True
    },"CSE", "maps/31x31/CSE.tmx", "art/CSE.png"
)
HOR = RoomBlueprint(
    {
        "north":False,
        "east":True,
        "south":False,
        "west":True
    },"HOR", "maps/31x31/HOR.tmx", "art/HOR.png"
)
VER = RoomBlueprint(
    {
        "north":True,
        "east":False,
        "south":True,
        "west":False
    },"VER", "maps/31x31/VER.tmx", "art/VER.png"
)
DEN = RoomBlueprint(
    {
        "north":True,
        "east":False,
        "south":False,
        "west":False,
    }, "DEN", "maps/31x31/DEN.tmx", "art/DEN.png"
)
DEE = RoomBlueprint(
    {
        "north":False,
        "east":True,
        "south":False,
        "west":False,
    }, "DEE", "maps/31x31/DEE.tmx", "art/DEE.png"
)
DES = RoomBlueprint(
    {
        "north":False,
        "east":False,
        "south":True,
        "west":False,
    }, "DES", "maps/31x31/DES.tmx", "art/DES.png"
)
DEW = RoomBlueprint(
    {
        "north":False,
        "east":False,
        "south":False,
        "west":True,
    }, "DEW", "maps/31x31/DEW.tmx", "art/DEW.png"
)
BLA = RoomBlueprint(
    {
        "north":False,
        "east":False,
        "south":False,
        "west":False
    }, "BLA", "maps/31x31/BLA.tmx", "art/BLA.png"
)
SDN = RoomBlueprint(
    {
        "north":True,
        "east":False,
        "south":False,
        "west":False,
    }, "SDN", "maps/31x31/SDN.tmx", "art/SDN.png"
)
SDE = RoomBlueprint(
    {
        "north":False,
        "east":True,
        "south":False,
        "west":False,
    }, "SDE", "maps/31x31/SDE.tmx", "art/SDE.png"
)
SDS = RoomBlueprint(
    {
        "north":False,
        "east":False,
        "south":True,
        "west":False,
    }, "SDS", "maps/31x31/SDS.tmx", "art/SDS.png"
)
SDW = RoomBlueprint(
    {
        "north":False,
        "east":False,
        "south":False,
        "west":True,
    }, "SDW", "maps/31x31/SDW.tmx", "art/SDW.png"
)

northRooms = [WES, ORI, EAS, CSW, SOU, CSE, VER, DEN]
southRooms = [CNW, NOR, CNE, WES, ORI, EAS, VER, DES]
eastRooms = [CNW, NOR, WES, ORI, CSW, SOU, HOR, DEE]
westRooms = [NOR, CNE, ORI, EAS, SOU, CSE, HOR, DEW]

class Floor:

    def __init__(self, mapGrid, mapSize):
        self.grid = mapGrid
        self.min = 0
        self.max = len(self.grid[0])-1
        self.floorDown = random.choice([SDN, SDE, SDS, SDW])
        self.activeStair = False
        self.mapSize = mapSize
        self.fillMap()
    
    def possibleRooms(self, possible, notPossible):
        
        a = self.possibleRoomsFunc(possible)
        if notPossible == []:
            return a
        else:
            b = self.possibleRoomsFunc(notPossible)
            # The following code was taken from https://stackoverflow.com/questions/13672543/removing-the-common-elements-between-two-lists
            # ----------------------------------------------------------
            return list(set(a).difference(b))
            # ----------------------------------------------------------

    def possibleRoomsFunc(self, directions):
        possibleLists = []
        for direction in directions:
            if direction == "north":
                possibleLists.append(northRooms)
            if direction == "east":
                possibleLists.append(eastRooms)
            if direction == "south":
                possibleLists.append(southRooms)
            if direction == "west":
                possibleLists.append(westRooms)
        
        # The following code was taken from https://www.geeksforgeeks.org/python-find-common-elements-in-list-of-lists/
        # ----------------------------------------------------------
        # Python3 code to demonstrate  
        # common element extraction from N lists  
        # using reduce() + lambda + set() 
        from functools import reduce
        
        # common element extraction form N lists 
        # using reduce() + lambda + set() 
        res = list(reduce(lambda i, j: i & j, (set(x) for x in possibleLists)))
        
        # returning result 
        return res
        # ----------------------------------------------------------

    def getRoom(self, direction, coords):
        if direction == "north":
            return self.grid[coords[0]-1][coords[1]]
        if direction == "east":
            return self.grid[coords[0]][coords[1]+1]
        if direction == "south":
            return self.grid[coords[0]+1][coords[1]]
        if direction == "west":
            return self.grid[coords[0]][coords[1]-1]

    def fillMap(self):
        # Fills in the corners as these will always be the same
        self.grid[self.min][self.min] = Room(CNW.info, self.min, self.min, self.mapSize)
        self.grid[self.min][self.max] = Room(CNE.info, self.min, self.max, self.mapSize)
        self.grid[self.max][self.min] = Room(CSW.info, self.max, self.min, self.mapSize)
        self.grid[self.max][self.max] = Room(CSE.info, self.max, self.max, self.mapSize)

        # Fills in the edges as they can be only one of 2 options
        for y in range(self.max+1):
            for x in range(self.max+1):
                location = (y, x)
                if location == (self.min, self.min) or location == (self.min, self.max) or location == (self.max, self.min) or location == (self.max, self.max):
                    pass
                else:
                    if location[0] == self.min:
                        possible = [HOR, NOR]
                        self.grid[location[0]][location[1]] = Room(random.choice(possible).info, location[0], location[1], self.mapSize)
                        
                    elif location[0] == self.max:
                        possible = [HOR, SOU]
                        self.grid[location[0]][location[1]] = Room(random.choice(possible).info, location[0], location[1], self.mapSize)
                        
                    elif location[1] == self.min:
                        possible = [VER, WES]
                        self.grid[location[0]][location[1]] = Room(random.choice(possible).info, location[0], location[1], self.mapSize)
                        
                    elif location[1] == self.max:
                        possible = [VER, EAS]
                        self.grid[location[0]][location[1]] = Room(random.choice(possible).info, location[0], location[1], self.mapSize)
                        
        # Fills in the centre
        for y in range(1,self.max+1):
            for x in range(self.max+1):
                location = (y, x)
                if location == (self.min, self.min) or location == (self.min, self.max) or location == (self.max, self.min) or location == (self.max, self.max) or location[0] == self.min or location[0] == self.max or location[1] == self.min or location[1] == self.max:
                    pass
                else:
                    if location[0] < self.max-1:
                        if isinstance(self.getRoom("east", location), str):
                            if self.getRoom("north", location).exit["south"]:
                                if self.getRoom("west", location).exit["east"]:
                                    # If room above and room to the left have openings
                                    possible = self.possibleRooms(["north", "west"], [])
                                    roomChoice = random.choice(possible)
                                    if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        self.activeStair = True
                                    else:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                    
                                else:
                                    # If only room above has opening
                                    possible = self.possibleRooms(["north"], ["west"])
                                    roomChoice = random.choice(possible)
                                    if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        self.activeStair = True
                                    else:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                    
                            else: 
                                if self.getRoom("west", location).exit["east"]:
                                    # If only room to the left has opening
                                    possible = self.possibleRooms(["west"], ["north"])
                                    roomChoice = random.choice(possible)
                                    if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        self.activeStair = True
                                    else:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                    
                                else:
                                    # If the room above and room to the left have no openings
                                    self.grid[location[0]][location[1]] = Room(CNW.info, location[0], location[1], self.mapSize)                          
                        else:
                            if self.getRoom("west", location).exit["east"]:
                                if self.getRoom("north", location).exit["south"]:
                                    if self.getRoom("east", location).exit["west"]: 
                                        # (111) If room above, to the left and to the right have openings:
                                        possible = self.possibleRooms(["north", "east", "west"], [])
                                        roomChoice = random.choice(possible)
                                        if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                            self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                            self.activeStair = True
                                        else:
                                            self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        
                                    else:
                                        # (110) If room above and room to left have openings, but room to right does not
                                        possible = self.possibleRooms(["north", "west"], ["east"])
                                        roomChoice = random.choice(possible)
                                        if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                            self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                            self.activeStair = True
                                        else:
                                            self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        
                                else:
                                    if self.getRoom("east", location).exit["west"]: 
                                        # (101) If room to the left and to the right have openings, but room above does not
                                        possible = self.possibleRooms(["east", "west"], ["north"])
                                        roomChoice = random.choice(possible)
                                        if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                            self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                            self.activeStair = True
                                        else:
                                            self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        
                                    else:
                                        # (100) If room to the left has opening, but room above and to right do not
                                        self.grid[location[0]][location[1]] = Room(CNE.info, location[0], location[1], self.mapSize)
                                        
                            else:
                                if self.getRoom("north", location).exit["south"]:
                                    if self.getRoom("east", location).exit["west"]: 
                                        # (011) If room above and room to the right have openings, but room to the left does not
                                        possible = self.possibleRooms(["north", "east"], ["west"])
                                        roomChoice = random.choice(possible)
                                        if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                            self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                            self.activeStair = True
                                        else:
                                            self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        
                                    else:
                                        # (010) If room above has opening, but room to the left and right do not
                                        self.grid[location[0]][location[1]] = Room(VER.info, location[0], location[1], self.mapSize)
                                        
                                else:
                                    if self.getRoom("east", location).exit["west"]: 
                                        # (001) If room to the right has opening, but room to the left and above do not
                                        self.grid[location[0]][location[1]] = Room(CNW.info, location[0], location[1], self.mapSize)
                                        
                                    else:
                                        # (000) If no rooms have openings
                                        self.grid[location[0]][location[1]] = Room(BLA.info, location[0], location[1], self.mapSize)
                                        
                    elif location[0] == self.max-1:
                        if location[1] == self.max-1:
                            if self.getRoom("north", location).exit["south"]:
                                if self.getRoom("east", location).exit["west"]:
                                    if self.getRoom("south", location).exit["north"]:
                                        if self.getRoom("west", location).exit["east"]:
                                            # (1111) If all rooms have openings
                                            self.grid[location[0]][location[1]] = Room(ORI.info, location[0], location[1], self.mapSize)
                                            
                                        else:
                                            # (1110) If room above, to the right and below have openings, but room to the left does not
                                            self.grid[location[0]][location[1]] = Room(WES.info, location[0], location[1], self.mapSize)
                                            
                                    else:
                                        if self.getRoom("west", location).exit["east"]:
                                            # (1101) If room above, to the left and right have openings, but room below does not
                                            self.grid[location[0]][location[1]] = Room(SOU.info, location[0], location[1], self.mapSize)
                                            
                                        else:
                                            # (1100) If room above and to the left have openings, but room below and to the right do not
                                            self.grid[location[0]][location[1]] = Room(CSW.info, location[0], location[1], self.mapSize)
                                            
                                else:
                                    if self.getRoom("south", location).exit["north"]:
                                        if self.getRoom("west", location).exit["east"]:
                                            # (1011) If room above, below and to the left have openings, but room to right does not
                                            self.grid[location[0]][location[1]] = Room(EAS.info, location[0], location[1], self.mapSize)
                                            
                                        else:
                                            # (1010) If room above and below have openings, but room to the left and right do not
                                            self.grid[location[0]][location[1]] = Room(VER.info, location[0], location[1], self.mapSize)
                                            
                                    else:
                                        if self.getRoom("west", location).exit["east"]:
                                            # (1001) If room above and to the left have openings, but room below and to the right do not
                                            self.grid[location[0]][location[1]] = Room(CSE.info, location[0], location[1], self.mapSize)
                                            
                                        else:
                                            # (1000) If room above has opening, but room below, to the left and right do not
                                            self.grid[location[0]][location[1]] = Room(DEN.info, location[0], location[1], self.mapSize)
                                            
                            else:
                                if self.getRoom("east", location).exit["west"]:
                                    if self.getRoom("south", location).exit["north"]:
                                        if self.getRoom("west", location).exit["east"]:
                                            # (0111) If room to the left, right and below have openings, but room above does not
                                            self.grid[location[0]][location[1]] = Room(NOR.info, location[0], location[1], self.mapSize)
                                            
                                        else:
                                            # (0110) If room to the right and below have openings, but room above and to the left do not
                                            self.grid[location[0]][location[1]] = Room(CNW.info, location[0], location[1], self.mapSize)
                                            
                                    else:
                                        if self.getRoom("west", location).exit["east"]:
                                            # (0101) If room to the left and right have openings, but room above and below do not
                                            self.grid[location[0]][location[1]] = Room(HOR.info, location[0], location[1], self.mapSize)
                                            
                                        else:
                                            # (0100) If room to the right has opening, but room above, to the left and below do not
                                            self.grid[location[0]][location[1]] = Room(DEE.info, location[0], location[1], self.mapSize)
                                            
                                else:
                                    if self.getRoom("south", location).exit["north"]:
                                        if self.getRoom("west", location).exit["east"]:
                                            # (0011)
                                            self.grid[location[0]][location[1]] = Room(CNE.info, location[0], location[1], self.mapSize)
                                            
                                        else:
                                            # (0010) If room below has opening, but room above, to the left and right do not
                                            self.grid[location[0]][location[1]] = Room(DES.info, location[0], location[1], self.mapSize)
                                            
                                    else:
                                        if self.getRoom("west", location).exit["east"]:
                                            # (0001) If room to the left has opening, but room above, below and to the right do not
                                            self.grid[location[0]][location[1]] = Room(DEW.info, location[0], location[1], self.mapSize)
                                            
                                        else:
                                            # (0000) If no rooms have openings
                                            self.grid[location[0]][location[1]] = Room(BLA.info, location[0], location[1], self.mapSize)
                                            
                        elif self.getRoom("north", location).exit["south"]:
                            if self.getRoom("west", location).exit["east"]:
                                if self.getRoom("south", location).exit["north"]:
                                    # (111) If room above, room to the left and room below have openings
                                    possible = self.possibleRooms(["west", "south", "north"], [])
                                    roomChoice = random.choice(possible)
                                    if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        self.activeStair = True
                                    else:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                else:
                                    # (110) If room above and room to the left have openings, but not room below
                                    possible = self.possibleRooms(["north", "west"], ["south"])
                                    roomChoice = random.choice(possible)
                                    if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        self.activeStair = True
                                    else:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                            else:
                                if self.getRoom("south", location).exit["north"]:
                                    # (101) If room above and room below have openings, but not room to the left
                                    possible = self.possibleRooms(["north", "south"], ["west"])
                                    roomChoice = random.choice(possible)
                                    if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        self.activeStair = True
                                    else:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                else:
                                    # (100) If room above has opening, but room to the left and below do not
                                    self.grid[location[0]][location[1]] = Room(CSW.info, location[0], location[1], self.mapSize)
                        else:
                            if self.getRoom("west", location).exit["east"]:
                                if self.getRoom("south", location).exit["north"]:
                                    # (011) If room to the left and below have openings, but room above does not
                                    possible = self.possibleRooms(["west", "south"], ["north"])
                                    roomChoice = random.choice(possible)
                                    if roomChoice in [SDN, SDE, SDS, SDW] and not self.activeStair:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                        self.activeStair = True
                                    else:
                                        self.grid[location[0]][location[1]] = Room(roomChoice.info, location[0], location[1], self.mapSize)
                                else:
                                    # (010) If room to the left has opening, but room above and below do not
                                    self.grid[location[0]][location[1]] = Room(HOR.info, location[0], location[1], self.mapSize)
                            else:
                                if self.getRoom("south", location).exit["north"]:
                                    # (001) If room below has opening, but room above and to the left do not
                                    self.grid[location[0]][location[1]] = Room(CNW.info, location[0], location[1], self.mapSize)
                                else:
                                    # (000) If no rooms have openings
                                    self.grid[location[0]][location[1]] = Room(BLA.info, location[0], location[1], self.mapSize)
            self.visual = []
            for row in self.grid:
                placeHolder = []
                for item in row:
                    if not isinstance(item, str):
                        placeHolder.append(item.name)
                    else:
                        placeHolder.append(item)
                self.visual.append(placeHolder)

class Dungeon:

    def __init__(self, floors, floorRadius, mapSize):
        self.numberOfFloors = floors
        self.floorRadius = floorRadius
        self.map = []
        for i in range(self.numberOfFloors):
            floor = Floor([["*" for i in range (self.floorRadius)] for i in range(self.floorRadius)], mapSize)
            self.map.append(floor)
        
        for floorNumber, floor in enumerate(self.map):
            temp = []
            for row in floor.grid:
               for room in row:
                   if room.name in ["DEN", "DEE", "DES", "DEW"]:
                       temp.append(room)
            roomToReplace = random.choice(temp)
            if roomToReplace.name == "DEN":
                staircase = SDN
            elif roomToReplace.name == "DEE":
                staircase = SDE
            elif roomToReplace.name == "DES":
                staircase = SDS
            elif roomToReplace.name == "DEW":
                staircase = SDW
            tempRoom = Room(staircase.info, roomToReplace.y, roomToReplace.x, mapSize)
            self.map[floorNumber].grid[roomToReplace.y][roomToReplace.x] = tempRoom
    
    def getRoom(self, direction, room, floor):
        if direction == "DOWN":
            try:
                return self.map[floor].grid[room[0]+1][room[1]]
            except IndexError:
                return None
        if direction == "UP":
            try:
                return self.map[floor].grid[room[0]-1][room[1]]
            except IndexError:
                return None
        if direction == "LEFT":
            try:
                return self.map[floor].grid[room[0]][room[1]-1]
            except IndexError:
                return None
        if direction == "RIGHT":
            try:
                return self.map[floor].grid[room[0]][room[1]+1]
            except IndexError:
                return None

    def removeDeadEnds(self):
        for floor in self.map:
            pass
