from eyezah import *
from eyezah.engine import *
from eyezah.world import Voxels

import time

mekal = Engine("mekal-engine")

print(mekal.move(UP).read())
time.sleep(1)
print(mekal.set(DOWN, Voxels.RED).read())
time.sleep(1)
print(mekal.move(UP).read())
time.sleep(1)
print(mekal.set_data(DOWN, "hello, world!").read())
time.sleep(1)

print(mekal.get_status().read())

