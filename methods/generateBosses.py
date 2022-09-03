from classes import enemy

def generateBosses(game):
    for floorNumber, floor in enumerate(game.dungeon.map):
        for rowNumber, row in enumerate(floor.grid):
            for columnNumber, room in enumerate(row):
                if room.name in ["SDN", "SDS", "SDE", "SDW"]:
                    # Is a stair down room
                    room.enemyDict = {}
                    room.enemyDict["boss0"] = enemy.Boss(50*(floorNumber+1), room, game)