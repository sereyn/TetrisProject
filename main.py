from qtido import *
from game import *
from tools import *

win = creer(800, 600)
FPS = 60

testBlock = Blocks.get("z")

print2DList(testBlock)
print2DList(Blocks.rotate(True, testBlock))

while not est_fermee(win):
	attendre_pendant(win, 1000/FPS)
