import tools
import qtido as qt
import Blocks
import game

qt.win = qt.creer(800, 600)
qt.win.widget.setWindowTitle("Tetris!")
FPS, TIME = 60, 0

gameBoard = tools.get2DGrid(20, 30)
testBlock = Blocks.get("t")
x, y = 0, 0

while not qt.est_fermee(qt.win):
	keys = qt.les_touches_appuyees(qt.win)
	right = tools.press("right", keys)
	left = tools.press("left", keys)
	x += right-left
	if TIME%20 == 0 or tools.press("down", keys):
		y += 1
	if tools.press("up", keys):
		testBlock = Blocks.rotate(testBlock)
	tools.clear(qt.win)
	temp = game.merge(gameBoard, testBlock, x, y)
	game.showGame(qt.win, temp, 15)
	TIME = tools.wait(qt.win, FPS, TIME)
