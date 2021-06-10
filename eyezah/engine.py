from urllib import request, parse

_base_url = "http://server.eyezah.tk:8002/voxelengine/api/"

NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"
UP = "up"
DOWN = "down"

class Voxels:
    AIR = 0
    DATA = 1
    RED = 2
    BLUE = 3
    ENGINE = 4

class Engine:
    def __init__(self, name):
        self.engineloc = "?engine=" + name

    def send(self, typ, data):
        print(_base_url + typ + self.engineloc + (parse.urlencode(data) if data is not None else ""))
        return request.urlopen(_base_url + typ + self.engineloc + (("&" + parse.urlencode(data)) if data is not None else ""))

    """
    Move the engine in the direction provided
    """
    def move(self, direction):
        return self.send("engine-move", {'direction': direction})

    """
    Sets a voxel with the specified type in the direction provided
    """
    def set(self, direction, typ):
        return self.send("voxel-set", {'direction': direction, 'type': typ})

    """
    Sets a data voxel with the specified data string in the direction provided
    """
    def set_data(self, direction, data):
        return self.send("voxel-set", {'direction': direction, 'type': Voxels.DATA, 'data': data})

    """
    Retrieve Data in a Status Around the Engine
    """
    def get_status(self):
        return self.send("engine-status", None)



