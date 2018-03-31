from tools import *
from qtS import *
import Blocks
from game import *

w = Window(800, 600, "Tetris", 60)

gameBoard = get2DGrid(20, 30)
testBlock = Blocks.get("t")
x, y = 0, 0

def update():
	global x, y, testBlock, gameBoard, w
	right = w.isPressed("right")
	left = w.isPressed("left")
	x += right-left
	if w.interval(20) or w.isPressed("down"):
		y += 1
	if w.isPressed("up"):
		testBlock = Blocks.rotate(testBlock)
	temp = merge(gameBoard, testBlock, x, y)
	showGame(w, temp, 15)

w.mainLoop(update)