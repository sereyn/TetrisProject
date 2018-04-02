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
	window.setColor(50, 50, 50)
	window.drawRect(0, 0, W*size, H*size)
	for i in range(W):
		for j in range(H):
			color = getColor(gB[j][i])
			window.setColor(*color)
			window.drawRect(size*i+1, size*j+1, size-2, size-2)
