from tools import *
from random import choice

# Legend: http://i.imgur.com/9Z0oJXe.png
def getBlockList(letter):
	if letter == "o":
		return [
			[1, 1],
			[1, 1]
		]
	if letter == "i":
		return [
			[0, 0, 0, 0],
			[2, 2, 2, 2],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	if letter == "j":
		return [
			[0, 0, 0],
			[3, 3, 3],
			[0, 0, 3]
		]
	if letter == "l":
		return [
			[0, 0, 0],
			[4, 4, 4],
			[4, 0, 0]
		]
	if letter == "s":
		return [
			[0, 0, 0],
			[0, 5, 5],
			[5, 5, 0],
		]
	if letter == "z":
		return [
			[0, 0, 0],
			[6, 6, 0],
			[0, 6, 6],
		]
	if letter == "t":
		return [
			[0, 0, 0],
			[7, 7, 7],
			[0, 7, 0],
		]

class Block(object):
	x, y = 10, 0
	def __init__(self):
		self.mat = getBlockList(choice(["o", "i", "j", "l", "s", "z", "t"]))
		self.x -= int(len(self.mat)/2)
	def rotate(self, inverse=False):
		if inverse:
			for i in range(3):
				self.rotate()
		else:
			N = len(self.mat)
			for x in range(0, int(N/2)):
				for y in range(x, N-x-1):
					temp = self.mat[x][y]
					self.mat[x][y] = self.mat[y][N-1-x]
					self.mat[y][N-1-x] = self.mat[N-1-x][N-1-y]
					self.mat[N-1-x][N-1-y] = self.mat[N-1-y][x]
					self.mat[N-1-y][x] = temp
	def hasProblem(self, gB):
		for i in range(len(self.mat[0])):
			for j in range(len(self.mat)):
				if self.mat[j][i] != 0:
					xx, yy = self.x+i, self.y+j
					if yy >= len(gB) or xx >= len(gB[0]) or xx < 0:
						return True
					else:
						if gB[yy][xx] != 0:
							return True
		return False
	def merge(self, gB):
		gB2 = clone2DList(gB)
		for i in range(len(self.mat[0])):
			for j in range(len(self.mat)):
				val = self.mat[j][i]
				if val != 0:
					xx, yy = self.x+i, self.y+j
					xInRange = xx >= 0 and xx < len(gB[0])
					yInRange = yy >= 0 and yy < len(gB)
					if xInRange and yInRange:
						gB2[yy][xx] = val
		return gB2
