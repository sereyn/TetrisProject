from btQt import *

def get2DGrid(w, h):
	l = []
	for i in range(h):
		temp = []
		for j in range(w):
			temp.append(0)
		l.append(temp)
	return l

def clone2DList(l):
	l2 = []
	for i in range(len(l)):
		sl = []
		for j in range(len(l[i])):
			sl.append(l[i][j])
		l2.append(sl)
	return l2

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

class GameBoard():
	emptyLines = []
	def __init__(self, cols, lines, cSize):
		self.grid = get2DGrid(cols, lines)
		self.cols, self.lines = cols, lines
		self.cSize = cSize
	def destroyLines(self):
		willReturn = False
		for i in self.emptyLines:
			for ii in range(i)[::-1]:
				for j in range(self.cols):
					self.grid[ii+1][j] = self.grid[ii][j]
			for j in range(self.cols):
				self.grid[0][j] = 0
			willReturn = True
		self.emptyLines = []
		for i in range(self.lines):
			isFull = True
			for j in range(self.cols):
				isFull &= self.grid[i][j] != 0
			if isFull:
				for j in range(self.cols):
					self.grid[i][j] = 0
				self.emptyLines.append(i)
		return willReturn
	def clone(self, copyContent=False):
		gB2 = GameBoard(self.cols, self.lines, self.cSize)
		if copyContent:
			gB2.grid = clone2DList(self.grid)
		return gB2
	def merge(self, gB, block):
		self.grid = clone2DList(gB.grid)
		for i in range(len(block.mat[0])):
			for j in range(len(block.mat)):
				val = block.mat[j][i]
				if val != 0:
					self.grid[block.y+j][block.x+i] = val
	def showGame(self, window):
		window.setColor(50, 50, 50)
		window.drawRect(0, 0, self.cols*self.cSize, self.lines*self.cSize)
		for i in range(self.cols):
			for j in range(self.lines):
				window.setColor(*getColor(self.grid[j][i]))
				window.drawRect(self.cSize*i+1, self.cSize*j+1, self.cSize-2, self.cSize-2)
