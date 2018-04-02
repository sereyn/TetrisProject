from btQt import *
from block import *
from board import *

cSize, cols, lines = 30, 20, 30
win = Window(cols*cSize, lines*cSize, "Tetris", 60)
# win.playSound("Data/bgm.mp3")
win.setIcon("Data/icon.png")

sndRotate = win.loadSFX("Data/rotate.mp3")
sndMove = win.loadSFX("Data/move.mp3")
sndDrop = win.loadSFX("Data/drop.mp3")
sndLine = win.loadSFX("Data/line.mp3")

gameBoard = GameBoard(cols, lines, cSize)
block = Block(gameBoard)

def update():
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
	tempBoard = gameBoard.clone()
	if block.hasProblem(gameBoard):
		block.y -= 1
		gameBoard.merge(gameBoard, block)
		block.newBlock()
		win.playSFX(sndDrop)
		tempBoard = gameBoard.clone(True)
	else:
		tempBoard.merge(gameBoard, block)
		tempBoard.addTransparentPiece(block)
	if win.interval(10):
		if gameBoard.destroyLines():
			win.playSFX(sndLine)
	tempBoard.showGame(win)

win.mainLoop(update)