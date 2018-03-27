from qtido import *
from game import *

win = creer(800, 600)
FPS = 60

print(Blocks.rotate(True, Blocks.z))

while not est_fermee(win):
	attendre_pendant(win, 1000/FPS)
