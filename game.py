from qtS import *
from tools import *

def getColor(num):
	colors = [
		[0, 0, 0],
		[255, 0, 0],
		[0, 255, 0],
		[0, 0, 255],
		[255, 255, 0],
		[0, 255, 255],
		[255, 0, 255],
		[255, 255, 255]
	]
	return colors[num]

def showGame(window, gB, size):
	H, W = len(gB), len(gB[0])
	for i in range(W):
		for j in range(H):
			color = getColor(gB[j][i])
			x, y = size*i, size*j
			window.setColor(50, 50, 50)
			window.drawRect(x, y, size, size)
			window.setColor(*color)
			window.drawRect(x+1, y+1, size-2, size-2)
