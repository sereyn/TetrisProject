import tools
import qtido as qt
import Blocks
import game

qt.win = qt.creer(800, 600)
qt.win.widget.setWindowTitle("Tetris!")
FPS = 2

gameBoard = tools.get2DGrid(10, 15)
testBlock = Blocks.get("t")
x, y = 0, 0

while not qt.est_fermee(qt.win):
	y += 1
	tools.clear(qt.win)
	temp = game.merge(gameBoard, testBlock, x, y)
	game.showGame(qt.win, temp, 30)
	qt.attendre_pendant(qt.win, 1000/FPS)
