from tools import *
from qtS import *
from Blocks import *
from game import *

cSize, cols, lines = 20, 20, 30
win = Window(cols*cSize, lines*cSize, "Tetris", 60)
win.playSound("Data/bgm.mp3")
win.setIcon("Data/icon.png")

sndRotate = win.loadSFX("Data/rotate.mp3")
sndMove = win.loadSFX("Data/move.mp3")
sndDrop = win.loadSFX("Data/drop.mp3")
sndLine = win.loadSFX("Data/line.mp3")

gameBoard = get2DGrid(cols, lines)
block = Block()

emptyLines = []

def checkLines(gB):
	global emptyLines
	for i in emptyLines:
		for ii in range(i)[::-1]:
			for j in range(len(gB[0])):
				gB[ii+1][j] = gB[ii][j]
		for j in range(len(gB[0])):
			gB[0][j] = 0
		win.playSFX(sndLine)
	emptyLines = []
	for i in range(len(gB)):
		isFull = True
		for j in range(len(gB[0])):
			isFull &= gB[i][j] != 0
		if isFull:
			for j in range(len(gB[0])):
				gB[i][j] = 0
			emptyLines.append(i)

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
		else:
			win.playSFX(sndRotate, True)
	if win.interval(5) or win.isPressed("down"):
		block.y += 1
		win.playSFX(sndMove)
	if block.hasProblem(gameBoard):
		block.y -= 1
		gameBoard = block.merge(gameBoard)
		block = Block()
		win.playSFX(sndDrop)
		tempBoard = gameBoard
	else:
		tempBoard = block.merge(gameBoard)
	if win.interval(10):
		checkLines(gameBoard)
	showGame(win, tempBoard, cSize)

win.mainLoop(update)