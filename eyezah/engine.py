from urllib import request, parse

_base_url = "http://server.eyezah.tk:8002/voxelengine/api/"

NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"
UP = "up"
DOWN = "down"

class Engine:
    def __init__(self, name):
        self.engineloc = "?engine=" + name + "&"

    def send(self, typ, data):
        return request.urlopen(_base_url + typ + self.engineloc + parse.urlencode(data))

    def move(self, direction):
        return self.send("engine-move", {'direction': direction})
    



