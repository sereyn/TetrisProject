from tools import *
from qtS import *
from Blocks import *
from game import *
from shutil import rmtree

cSize, cols, lines = 20, 20, 30
win = Window(cols*cSize, lines*cSize, "Tetris", 60)

gameBoard = get2DGrid(cols, lines)
block = Block()

def update():
	global gameBoard, block
	right = win.isJustPressed("right") or win.isPressedSince("right", 5)
	left = win.isJustPressed("left") or win.isPressedSince("left", 5)
	block.x += right-left
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
		block = Block()
	else:
		tempBoard = block.merge(gameBoard)
	showGame(win, tempBoard, cSize)

win.mainLoop(update)
rmtree("__pycache__")