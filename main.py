from tools import *
from qtS import *
from Blocks import *
from game import *

cSize, cols, lines = 20, 20, 30
win = Window(cols*cSize, lines*cSize, "Tetris", 60)
win.playSound("Data/bgm.mp3")
win.setIcon("Data/icon.png")

gameBoard = get2DGrid(cols, lines)
block = Block()

def update():
	global gameBoard, block
	right = win.isJustPressed("right") or win.isPressedSince("right", 5)
	left = win.isJustPressed("left") or win.isPressedSince("left", 5)
	block.x += right-left
	if block.hasProblem(gameBoard):
		block.x -= right-left
	if win.isJustPressed("up"):
		block.rotate()
	if block.hasProblem(gameBoard):
		block.rotate(True)
	if win.interval(10) or win.isPressed("down"):
		block.y += 1
	if block.hasProblem(gameBoard):
		block.y -= 1
		gameBoard = tempBoard = block.merge(gameBoard)
		block = Block()
	else:
		tempBoard = block.merge(gameBoard)
	showGame(win, tempBoard, cSize)

win.mainLoop(update)