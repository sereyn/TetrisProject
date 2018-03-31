from tools import *
from qtS import *
from Blocks import *
from game import *
from random import choice
from shutil import rmtree

cSize, cols, lines = 20, 20, 30
win = Window(cols*cSize, lines*cSize, "Tetris", 60)

gameBoard = get2DGrid(cols, lines)
blocks = ["o", "i", "j", "l", "s", "z", "t"]
block = Block(choice(blocks))

def update():
	global win, gameBoard, block, cSize
	block.x += win.isPressed("right")-win.isPressed("left")
	if win.interval(10) or win.isPressed("down"):
		block.y += 1
	if win.isJustPressed("up"):
		block.rotate()
	tooLow, tooRight, tooLeft, collide = block.checkPosition(gameBoard)
	block.x += tooLeft-tooRight
	if tooLow:
		block.y -= 1
		tempBoard = block.merge(gameBoard)
		gameBoard = tempBoard
		block = Block(choice(blocks))
	else:
		tempBoard = block.merge(gameBoard)
	showGame(win, tempBoard, cSize)

win.mainLoop(update)
rmtree("__pycache__")